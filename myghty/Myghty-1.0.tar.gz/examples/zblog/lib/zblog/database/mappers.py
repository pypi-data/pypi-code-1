"""mapper.py - defines mappers for domain objects, mapping operations"""

import zblog.database.tables as tables
import zblog.domain.user as user
from zblog.domain.blog import *
from sqlalchemy import *

# User mapper.  Here, we redefine the names of some of the columns
# to different property names.  normally the table columns are all
# sucked in automatically.
user.User.mapper = mapper(user.User, tables.users, properties={
    'id':tables.users.c.user_id,
    'name':tables.users.c.user_name,
    'group':tables.users.c.groupname,
    'crypt_password':tables.users.c.password,
})

# blog mapper.  this contains a reference to the user mapper,
# and also installs a "backreference" on that relationship to handle it
# in both ways. this will also attach a 'blogs' property to the user mapper.
Blog.mapper = mapper(Blog, tables.blogs, properties={
    'id':tables.blogs.c.blog_id,
    'owner':relation(user.User, lazy=False, backref='blogs'),
}, is_primary=True)

# override the 'blogs' property on the user mapper to be a "private" relation,
# which means the blogs only exist as children of that user.  remove the blog
# from the user's list, it gets deleted; delete the user, the blogs get deleted.
user.User.mapper.add_property('blogs', relation(Blog.mapper, private=True, lazy=True, backref='owner')) 

# topic mapper.  map all topic columns to the Topic class.
Topic.mapper = mapper(Topic, tables.topics)
        
# TopicAssocation mapper.  This is an "association" object, which is similar to
# a many-to-many relationship except extra data is associated with each pair 
# of related data.  because the topic_xref table doesnt have a primary key,
# the "primary key" columns of a TopicAssociation are defined manually here.
TopicAssociation.mapper = mapper(TopicAssociation,tables.topic_xref, 
                primary_key=[tables.topic_xref.c.post_id, tables.topic_xref.c.topic_id], 
                properties={
                    'topic':relation(Topic.mapper, lazy=False),
                })

# Post mapper, these are posts within a blog.  
# since we want the count of comments for each post, create a select that will get the posts
# and count the comments in one query.
posts_with_ccount = select(
    [c for c in tables.posts.c if c.key != 'body'] + [
        func.count(tables.comments.c.comment_id).label('comment_count')
    ],
    from_obj = [
        outerjoin(tables.posts, tables.comments)
    ],
    group_by=[
        c for c in tables.posts.c
    ]
    ) .alias('postswcount')

# then create a Post mapper on that query.  
# we have the body as "deferred" so that it loads only when needed,
# the user as a Lazy load, since the lazy load will run only once per user and
# its usually only one user's posts is needed per page,
# the owning blog is a lazy load since its also probably loaded into the identity map
# already, and topics is an eager load since that query has to be done per post in any
# case.
Post.mapper = mapper(Post, posts_with_ccount, properties={
    'id':posts_with_ccount.c.post_id,
    'body':deferred(tables.posts.c.body),
    'user':relation(user.User, lazy=True, backref='posts'),
    'blog':relation(Blog, lazy=True, backref='posts'),
    'topics':relation(TopicAssociation, lazy=False, private=True, association=Topic)
}, is_primary=True, order_by=[desc(posts_with_ccount.c.datetime)])

# override 'posts' property on Blog to be private, so that posts get deleted when the blog does.
Blog.mapper.add_property('posts', relation(Post.mapper, private=True, lazy=True, backref='blog'))

# override 'posts' property on User to be private, so all user posts in all blogs get
# removed when the user does.
user.User.mapper.add_property('posts', relation(Post.mapper, private=True, lazy=True, backref='user'))

# comment mapper.  This mapper is handling a hierarchical relationship on itself, and contains
# a lazy reference both to its parent comment and its list of child comments.
Comment.mapper = mapper(Comment, tables.comments, properties={
    'id':tables.comments.c.comment_id,
    'post':relation(Post.mapper, lazy=True, backref='comments'),
    'user':relation(user.User.mapper, lazy=False, backref='comments'),
    'parent':relation(Comment, primaryjoin=tables.comments.c.parent_comment_id==tables.comments.c.comment_id, foreignkey=tables.comments.c.comment_id, lazy=True, uselist=False),
    'replies':relation(Comment,primaryjoin=tables.comments.c.parent_comment_id==tables.comments.c.comment_id, lazy=True, uselist=True, private=True),
}, is_primary=True)

# override the "post" and "user" backreference-generated properties to be lazy properties
Post.mapper.add_property('comments', relation(Comment.mapper, private=True, lazy=True, backref='post'))
user.User.mapper.add_property('comments', relation(Comment.mapper, private=True, lazy=True, backref='user'))

# we define one special find-by for the comments of a post, which is going to make its own "noload"
# mapper and organize the comments into their correct hierarchy in one pass. hierarchical
# data normally needs to be loaded by separate queries for each set of children, unless you
# use a proprietary extension like CONNECT BY.
def find_by_post(post):
    """returns a hierarchical collection of comments based on a given criterion.  
    uses a mapper that does not lazy load replies or parents, and instead
    organizes comments into a hierarchical tree when the result is produced.
    """
    mapper = Comment.mapper.options(noload('replies'), noload('parent'))
    comments = mapper.select_by(post_id=post.id)
    result = []
    d = {}
    for c in comments:
        d[c.id] = c
        if c.parent_comment_id is None:
            result.append(c)
            c.parent=None
        else:
            parent = d[c.parent_comment_id]
            parent.replies.append(c)
            c.parent = parent
    return result

Comment.find_by_post = staticmethod(find_by_post)

# define a bunch of convenience methods on the objectstore.

def start_session():
    """clears the objectstore, so that when a new user request is handled, all data will be
    loaded from the database completely, and anything left over from the previous session
    is removed.  Clearing the objectstore is a thread-local operation."""
    objectstore.clear()
    
def begin():
    """begins a transaction with the objectstore."""
    objectstore.begin()

def commit():
    """commits a transaction with the objectstore.  everything modified since the last
    begin() is updated in the database."""
    print "\n\n------------------------------\n\n"
    objectstore.commit()
    
def delete(*obj):
    """marks an object (or objects) to be deleted upon the next commit()."""
    objectstore.delete(*obj)
    
    
