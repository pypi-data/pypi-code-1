# $Id: printenv.html.py,v 1.1 2002/05/02 00:11:56 jribbens Exp $


class main(wt.TemplateCode):
  class request(wt.TemplateCode):
    def main(self, template):
      for (self.key, self.val) in self.req.params.iteritems():
        self.process(template)

  class cookies(wt.TemplateCode):
    def main(self, template):
      for (self.key, self.val) in self.req.cookies.iteritems():
        self.process(template)

  class environ(wt.TemplateCode):
    def main(self, template):
      for (self.key, self.val) in self.req.environ.iteritems():
        self.process(template)
