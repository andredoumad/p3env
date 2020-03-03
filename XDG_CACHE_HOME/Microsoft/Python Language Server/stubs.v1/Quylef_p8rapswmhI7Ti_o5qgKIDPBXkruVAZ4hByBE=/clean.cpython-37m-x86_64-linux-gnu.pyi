import builtins as _mod_builtins
import re as _mod_re

class Cleaner(_mod_builtins.object):
    '\n    Instances cleans the document of each of the possible offending\n    elements.  The cleaning is controlled by attributes; you can\n    override attributes in a subclass, or set them in the constructor.\n\n    ``scripts``:\n        Removes any ``<script>`` tags.\n\n    ``javascript``:\n        Removes any Javascript, like an ``onclick`` attribute. Also removes stylesheets\n        as they could contain Javascript.\n\n    ``comments``:\n        Removes any comments.\n\n    ``style``:\n        Removes any style tags.\n\n    ``inline_style``\n        Removes any style attributes.  Defaults to the value of the ``style`` option.\n\n    ``links``:\n        Removes any ``<link>`` tags\n\n    ``meta``:\n        Removes any ``<meta>`` tags\n\n    ``page_structure``:\n        Structural parts of a page: ``<head>``, ``<html>``, ``<title>``.\n\n    ``processing_instructions``:\n        Removes any processing instructions.\n\n    ``embedded``:\n        Removes any embedded objects (flash, iframes)\n\n    ``frames``:\n        Removes any frame-related tags\n\n    ``forms``:\n        Removes any form tags\n\n    ``annoying_tags``:\n        Tags that aren\'t *wrong*, but are annoying.  ``<blink>`` and ``<marquee>``\n\n    ``remove_tags``:\n        A list of tags to remove.  Only the tags will be removed,\n        their content will get pulled up into the parent tag.\n\n    ``kill_tags``:\n        A list of tags to kill.  Killing also removes the tag\'s content,\n        i.e. the whole subtree, not just the tag itself.\n\n    ``allow_tags``:\n        A list of tags to include (default include all).\n\n    ``remove_unknown_tags``:\n        Remove any tags that aren\'t standard parts of HTML.\n\n    ``safe_attrs_only``:\n        If true, only include \'safe\' attributes (specifically the list\n        from the feedparser HTML sanitisation web site).\n\n    ``safe_attrs``:\n        A set of attribute names to override the default list of attributes\n        considered \'safe\' (when safe_attrs_only=True).\n\n    ``add_nofollow``:\n        If true, then any <a> tags will have ``rel="nofollow"`` added to them.\n\n    ``host_whitelist``:\n        A list or set of hosts that you can use for embedded content\n        (for content like ``<object>``, ``<link rel="stylesheet">``, etc).\n        You can also implement/override the method\n        ``allow_embedded_url(el, url)`` or ``allow_element(el)`` to\n        implement more complex rules for what can be embedded.\n        Anything that passes this test will be shown, regardless of\n        the value of (for instance) ``embedded``.\n\n        Note that this parameter might not work as intended if you do not\n        make the links absolute before doing the cleaning.\n\n        Note that you may also need to set ``whitelist_tags``.\n\n    ``whitelist_tags``:\n        A set of tags that can be included with ``host_whitelist``.\n        The default is ``iframe`` and ``embed``; you may wish to\n        include other tags like ``script``, or you may want to\n        implement ``allow_embedded_url`` for more control.  Set to None to\n        include all tags.\n\n    This modifies the document *in place*.\n    '
    def __call__(self, doc):
        '\n        Cleans the document.\n        '
        pass
    
    __class__ = Cleaner
    __dict__ = {}
    def __init__(self, **kw):
        '\n    Instances cleans the document of each of the possible offending\n    elements.  The cleaning is controlled by attributes; you can\n    override attributes in a subclass, or set them in the constructor.\n\n    ``scripts``:\n        Removes any ``<script>`` tags.\n\n    ``javascript``:\n        Removes any Javascript, like an ``onclick`` attribute. Also removes stylesheets\n        as they could contain Javascript.\n\n    ``comments``:\n        Removes any comments.\n\n    ``style``:\n        Removes any style tags.\n\n    ``inline_style``\n        Removes any style attributes.  Defaults to the value of the ``style`` option.\n\n    ``links``:\n        Removes any ``<link>`` tags\n\n    ``meta``:\n        Removes any ``<meta>`` tags\n\n    ``page_structure``:\n        Structural parts of a page: ``<head>``, ``<html>``, ``<title>``.\n\n    ``processing_instructions``:\n        Removes any processing instructions.\n\n    ``embedded``:\n        Removes any embedded objects (flash, iframes)\n\n    ``frames``:\n        Removes any frame-related tags\n\n    ``forms``:\n        Removes any form tags\n\n    ``annoying_tags``:\n        Tags that aren\'t *wrong*, but are annoying.  ``<blink>`` and ``<marquee>``\n\n    ``remove_tags``:\n        A list of tags to remove.  Only the tags will be removed,\n        their content will get pulled up into the parent tag.\n\n    ``kill_tags``:\n        A list of tags to kill.  Killing also removes the tag\'s content,\n        i.e. the whole subtree, not just the tag itself.\n\n    ``allow_tags``:\n        A list of tags to include (default include all).\n\n    ``remove_unknown_tags``:\n        Remove any tags that aren\'t standard parts of HTML.\n\n    ``safe_attrs_only``:\n        If true, only include \'safe\' attributes (specifically the list\n        from the feedparser HTML sanitisation web site).\n\n    ``safe_attrs``:\n        A set of attribute names to override the default list of attributes\n        considered \'safe\' (when safe_attrs_only=True).\n\n    ``add_nofollow``:\n        If true, then any <a> tags will have ``rel="nofollow"`` added to them.\n\n    ``host_whitelist``:\n        A list or set of hosts that you can use for embedded content\n        (for content like ``<object>``, ``<link rel="stylesheet">``, etc).\n        You can also implement/override the method\n        ``allow_embedded_url(el, url)`` or ``allow_element(el)`` to\n        implement more complex rules for what can be embedded.\n        Anything that passes this test will be shown, regardless of\n        the value of (for instance) ``embedded``.\n\n        Note that this parameter might not work as intended if you do not\n        make the links absolute before doing the cleaning.\n\n        Note that you may also need to set ``whitelist_tags``.\n\n    ``whitelist_tags``:\n        A set of tags that can be included with ``host_whitelist``.\n        The default is ``iframe`` and ``embed``; you may wish to\n        include other tags like ``script``, or you may want to\n        implement ``allow_embedded_url`` for more control.  Set to None to\n        include all tags.\n\n    This modifies the document *in place*.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'lxml.html.clean'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def _has_sneaky_javascript(self, style):
        '\n        Depending on the browser, stuff like ``e x p r e s s i o n(...)``\n        can get interpreted, or ``expre/* stuff */ssion(...)``.  This\n        checks for attempt to do stuff like this.\n\n        Typically the response will be to kill the entire style; if you\n        have just a bit of Javascript in the style another rule will catch\n        that and remove only the Javascript from the style; this catches\n        more sneaky attempts.\n        '
        pass
    
    def _kill_elements(self, doc, condition, iterate):
        pass
    
    def _remove_javascript_link(self, link):
        pass
    
    @classmethod
    def _substitute_comments(cls, self, repl, string, count):
        'Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl.'
        pass
    
    _tag_link_attrs = _mod_builtins.dict()
    add_nofollow = False
    def allow_element(self, el):
        pass
    
    def allow_embedded_url(self, el, url):
        pass
    
    def allow_follow(self, anchor):
        '\n        Override to suppress rel="nofollow" on some anchors.\n        '
        pass
    
    allow_tags = None
    annoying_tags = True
    def clean_html(self, html):
        pass
    
    comments = True
    embedded = True
    forms = True
    frames = True
    host_whitelist = _mod_builtins.tuple()
    inline_style = None
    javascript = True
    def kill_conditional_comments(self, doc):
        "\n        IE conditional comments basically embed HTML that the parser\n        doesn't normally see.  We can't allow anything like that, so\n        we'll kill any comments that could be conditional.\n        "
        pass
    
    kill_tags = None
    links = True
    meta = True
    page_structure = True
    processing_instructions = True
    remove_tags = None
    remove_unknown_tags = True
    safe_attrs = _mod_builtins.frozenset()
    safe_attrs_only = True
    scripts = True
    style = False
    whitelist_tags = _mod_builtins.set()

XHTML_NAMESPACE = 'http://www.w3.org/1999/xhtml'
__all__ = _mod_builtins.list()
__builtins__ = {}
__doc__ = 'A cleanup tool for HTML.\n\nRemoves unwanted tags and content.  See the `Cleaner` class for\ndetails.\n'
__file__ = '/home/gordon/p3env/lib/python3.7/site-packages/lxml/html/clean.cpython-37m-x86_64-linux-gnu.so'
__name__ = 'lxml.html.clean'
__package__ = 'lxml.html'
__test__ = _mod_builtins.dict()
_avoid_classes = _mod_builtins.list()
_avoid_elements = _mod_builtins.list()
_avoid_hosts = _mod_builtins.list()
_avoid_word_break_classes = _mod_builtins.list()
_avoid_word_break_elements = _mod_builtins.list()
_break_prefer_re = _mod_re.Pattern()
def _break_text(text, max_width, break_character):
    pass

_conditional_comment_re = _mod_re.Pattern()
_css_import_re = _mod_re.Pattern()
_css_javascript_re = _mod_re.Pattern()
def _find_external_links():
    "XPath(self, path, namespaces=None, extensions=None, regexp=True, smart_strings=True)\n    A compiled XPath expression that can be called on Elements and ElementTrees.\n\n    Besides the XPath expression, you can pass prefix-namespace\n    mappings and extension functions to the constructor through the\n    keyword arguments ``namespaces`` and ``extensions``.  EXSLT\n    regular expression support can be disabled with the 'regexp'\n    boolean keyword (defaults to True).  Smart strings will be\n    returned for string results unless you pass\n    ``smart_strings=False``.\n    "
    pass

def _find_styled_elements():
    "XPath(self, path, namespaces=None, extensions=None, regexp=True, smart_strings=True)\n    A compiled XPath expression that can be called on Elements and ElementTrees.\n\n    Besides the XPath expression, you can pass prefix-namespace\n    mappings and extension functions to the constructor through the\n    keyword arguments ``namespaces`` and ``extensions``.  EXSLT\n    regular expression support can be disabled with the 'regexp'\n    boolean keyword (defaults to True).  Smart strings will be\n    returned for string results unless you pass\n    ``smart_strings=False``.\n    "
    pass

def _insert_break(word, width, break_character):
    pass

def _is_image_dataurl(self, string, pos, endpos):
    'Scan through string looking for a match, and return a corresponding match object instance.\n\nReturn None if no position in the string matches.'
    pass

def _is_javascript_scheme(s):
    pass

def _is_possibly_malicious_scheme(self, string, pos, endpos):
    'Scan through string looking for a match, and return a corresponding match object instance.\n\nReturn None if no position in the string matches.'
    pass

_link_regexes = _mod_builtins.list()
def _link_text(text, link_regexes, avoid_hosts, factory):
    pass

def _substitute_whitespace(self, repl, string, count):
    'Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl.'
    pass

def _transform_result(typ, result):
    'Convert the result back into the input type.\n    '
    pass

def autolink(el, link_regexes, avoid_elements, avoid_hosts, avoid_classes):
    "\n    Turn any URLs into links.\n\n    It will search for links identified by the given regular\n    expressions (by default mailto and http(s) links).\n\n    It won't link text in an element in avoid_elements, or an element\n    with a class in avoid_classes.  It won't link to anything with a\n    host that matches one of the regular expressions in avoid_hosts\n    (default localhost and 127.0.0.1).\n\n    If you pass in an element, the element's tail will not be\n    substituted, only the contents of the element.\n    "
    pass

def autolink_html(html, *args, **kw):
    "\n    Turn any URLs into links.\n\n    It will search for links identified by the given regular\n    expressions (by default mailto and http(s) links).\n\n    It won't link text in an element in avoid_elements, or an element\n    with a class in avoid_classes.  It won't link to anything with a\n    host that matches one of the regular expressions in avoid_hosts\n    (default localhost and 127.0.0.1).\n\n    If you pass in an element, the element's tail will not be\n    substituted, only the contents of the element.\n    "
    pass

basestring = _mod_builtins.tuple()
def clean(self, doc):
    '\n    Instances cleans the document of each of the possible offending\n    elements.  The cleaning is controlled by attributes; you can\n    override attributes in a subclass, or set them in the constructor.\n\n    ``scripts``:\n        Removes any ``<script>`` tags.\n\n    ``javascript``:\n        Removes any Javascript, like an ``onclick`` attribute. Also removes stylesheets\n        as they could contain Javascript.\n\n    ``comments``:\n        Removes any comments.\n\n    ``style``:\n        Removes any style tags.\n\n    ``inline_style``\n        Removes any style attributes.  Defaults to the value of the ``style`` option.\n\n    ``links``:\n        Removes any ``<link>`` tags\n\n    ``meta``:\n        Removes any ``<meta>`` tags\n\n    ``page_structure``:\n        Structural parts of a page: ``<head>``, ``<html>``, ``<title>``.\n\n    ``processing_instructions``:\n        Removes any processing instructions.\n\n    ``embedded``:\n        Removes any embedded objects (flash, iframes)\n\n    ``frames``:\n        Removes any frame-related tags\n\n    ``forms``:\n        Removes any form tags\n\n    ``annoying_tags``:\n        Tags that aren\'t *wrong*, but are annoying.  ``<blink>`` and ``<marquee>``\n\n    ``remove_tags``:\n        A list of tags to remove.  Only the tags will be removed,\n        their content will get pulled up into the parent tag.\n\n    ``kill_tags``:\n        A list of tags to kill.  Killing also removes the tag\'s content,\n        i.e. the whole subtree, not just the tag itself.\n\n    ``allow_tags``:\n        A list of tags to include (default include all).\n\n    ``remove_unknown_tags``:\n        Remove any tags that aren\'t standard parts of HTML.\n\n    ``safe_attrs_only``:\n        If true, only include \'safe\' attributes (specifically the list\n        from the feedparser HTML sanitisation web site).\n\n    ``safe_attrs``:\n        A set of attribute names to override the default list of attributes\n        considered \'safe\' (when safe_attrs_only=True).\n\n    ``add_nofollow``:\n        If true, then any <a> tags will have ``rel="nofollow"`` added to them.\n\n    ``host_whitelist``:\n        A list or set of hosts that you can use for embedded content\n        (for content like ``<object>``, ``<link rel="stylesheet">``, etc).\n        You can also implement/override the method\n        ``allow_embedded_url(el, url)`` or ``allow_element(el)`` to\n        implement more complex rules for what can be embedded.\n        Anything that passes this test will be shown, regardless of\n        the value of (for instance) ``embedded``.\n\n        Note that this parameter might not work as intended if you do not\n        make the links absolute before doing the cleaning.\n\n        Note that you may also need to set ``whitelist_tags``.\n\n    ``whitelist_tags``:\n        A set of tags that can be included with ``host_whitelist``.\n        The default is ``iframe`` and ``embed``; you may wish to\n        include other tags like ``script``, or you may want to\n        implement ``allow_embedded_url`` for more control.  Set to None to\n        include all tags.\n\n    This modifies the document *in place*.\n    '
    pass

def clean_html(self, html):
    pass

def fromstring(html, base_url, parser, **kw):
    "\n    Parse the html, returning a single element/document.\n\n    This tries to minimally parse the chunk of text, without knowing if it\n    is a fragment or a document.\n\n    base_url will set the document's base_url attribute (and the tree's docinfo.URL)\n    "
    pass

def unichr(i):
    'Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.'
    pass

unicode = _mod_builtins.str
def urlsplit(url, scheme, allow_fragments):
    "Parse a URL into 5 components:\n    <scheme>://<netloc>/<path>?<query>#<fragment>\n    Return a 5-tuple: (scheme, netloc, path, query, fragment).\n    Note that we don't break the components up in smaller bits\n    (e.g. netloc is a single string) and we don't expand % escapes."
    pass

def word_break(el, max_width, avoid_elements, avoid_classes, break_character):
    "\n    Breaks any long words found in the body of the text (not attributes).\n\n    Doesn't effect any of the tags in avoid_elements, by default\n    ``<textarea>`` and ``<pre>``\n\n    Breaks words by inserting &#8203;, which is a unicode character\n    for Zero Width Space character.  This generally takes up no space\n    in rendering, but does copy as a space, and in monospace contexts\n    usually takes up space.\n\n    See http://www.cs.tut.fi/~jkorpela/html/nobr.html for a discussion\n    "
    pass

def word_break_html(html, *args, **kw):
    pass

def xhtml_to_html(xhtml):
    'Convert all tags in an XHTML tree to HTML by removing their\n    XHTML namespace.\n    '
    pass

