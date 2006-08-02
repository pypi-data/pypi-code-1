__all__ = ["TinyMCE"]

import re
import pkg_resources

from turbojson.jsonify import encode
from turbogears.widgets import JSSource, JSLink, TextArea, WidgetDescription, \
                               register_static_directory
from turbogears.validators import FancyValidator



js_dir = pkg_resources.resource_filename("tinymce", "static/javascript")
register_static_directory("tinymce", js_dir)






class HTMLCleaner(FancyValidator):
    """Strips off the ugly <br />s TinyMCE leaves the end of pasted text"""
    cleaner = re.compile(r'(\s*<br />\s*)+$').sub 
    def to_python(self, value, state=None):
        return self.cleaner('', value)





class TinyMCE(TextArea):
    """WYSIWYG editor for textareas. You can pass options directly to TinyMCE
    at consruction or display time via the 'mce_options' dict parameter.
    """
    template = """
    <span xmlns:py="http://purl.org/kid/ns#">
        <textarea
            name="${name}"
            class="${field_class}"
            id="${field_id}"
            rows="${rows}"
            cols="${cols}"
            py:attrs="attrs"
            py:content="value"
        />
        <script type="text/javascript">${TinyMCEInit}</script>
    </span>
    """
    params = ["mce_options"]
    rows = 25
    mce_options = dict(
        mode = "exact",
        theme = "advanced",
        plugins = "advimage",
        theme_advanced_toolbar_location = "top",
        theme_advanced_toolbar_align = "center",
        theme_advanced_statusbar_location = "bottom",
        extended_valid_elements = "a[href|target|name]",
        theme_advanced_resizing = True,
        paste_use_dialog = False,
        paste_auto_cleanup_on_paste = True,
        paste_convert_headers_to_strong = False,
        paste_strip_class_attributes = "all",
    )
    validator = HTMLCleaner()
    javascript = [JSLink("tinymce", "tiny_mce_src.js")]

    def update_params(self, d):
        super(TinyMCE, self).update_params(d)
        d['mce_options']['elements'] = d['field_id']
        d['TinyMCEInit'] = "tinyMCE.init(%s);" % encode(d['mce_options'])



class TinyMCEDesc(WidgetDescription):
    name = "TinyMCE"
    for_widget = TinyMCE("mce_sample")
    value = "<h1>This is some sample text.</h1>Edit me as you please."
