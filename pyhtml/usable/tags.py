from pyhtml.dtype.base import TagTypeEnum
from pyhtml.dtype.facotry import Factory

# base
HTML = Factory.create_tag(TagTypeEnum.UNALLOCATED, 'html', True)
HEAD = Factory.create_tag(TagTypeEnum.UNALLOCATED, 'head', True)
BODY = Factory.create_tag(TagTypeEnum.UNALLOCATED, 'body', True)
TITLE = Factory.create_tag(TagTypeEnum.HEAD, 'title', True)
H1 = Factory.create_tag(TagTypeEnum.BODY, 'h1', True)
H2 = Factory.create_tag(TagTypeEnum.BODY, 'h2', True)
H3 = Factory.create_tag(TagTypeEnum.BODY, 'h3', True)
H4 = Factory.create_tag(TagTypeEnum.BODY, 'h4', True)
H5 = Factory.create_tag(TagTypeEnum.BODY, 'h5', True)
H6 = Factory.create_tag(TagTypeEnum.BODY, 'h6', True)
P = Factory.create_tag(TagTypeEnum.BODY, 'p', True)
BR = Factory.create_tag(TagTypeEnum.BODY, 'br', False)
HR = Factory.create_tag(TagTypeEnum.BODY, 'hr', False)

# formating
ABBR = Factory.create_tag(TagTypeEnum.BODY, 'abbr', True)
ADDRESS = Factory.create_tag(TagTypeEnum.BODY, 'address', True)
B = Factory.create_tag(TagTypeEnum.BODY, 'b', True)
BLOCKQUOTE = Factory.create_tag(TagTypeEnum.BODY, 'blockquote', True)
CITE = Factory.create_tag(TagTypeEnum.BODY, 'cite', True)
CODE = Factory.create_tag(TagTypeEnum.BODY, 'code', True)
I = Factory.create_tag(TagTypeEnum.BODY, 'i', True)
MARK = Factory.create_tag(TagTypeEnum.BODY, 'mark', True)
PROGRESS = Factory.create_tag(TagTypeEnum.BODY, 'progress', True)
RUBY = Factory.create_tag(TagTypeEnum.BODY, 'ruby', True)
SAMP = Factory.create_tag(TagTypeEnum.BODY, 'samp', True)
SMALL = Factory.create_tag(TagTypeEnum.BODY, 'small', True)
STRONG = Factory.create_tag(TagTypeEnum.BODY, 'strong', True)
TEMPLATE = Factory.create_tag(TagTypeEnum.BODY, 'template', True)
TIME = Factory.create_tag(TagTypeEnum.BODY, 'time', True)
U = Factory.create_tag(TagTypeEnum.BODY, 'u', True)

# form
FORM = Factory.create_tag(TagTypeEnum.BODY, 'form', True)
INPUT = Factory.create_tag(TagTypeEnum.BODY, 'input', False)
TEXTAREA = Factory.create_tag(TagTypeEnum.BODY, 'textarea', True)
BUTTON = Factory.create_tag(TagTypeEnum.BODY, 'button', True)
SELECT = Factory.create_tag(TagTypeEnum.BODY, 'select', True)
OPTGROUP = Factory.create_tag(TagTypeEnum.BODY, 'optgroup', True)
OPTION = Factory.create_tag(TagTypeEnum.BODY, 'option', True)
LABEL = Factory.create_tag(TagTypeEnum.BODY, 'label', True)
FIELDSET = Factory.create_tag(TagTypeEnum.BODY, 'fieldset', True)
LEGEND = Factory.create_tag(TagTypeEnum.BODY, 'legend', True)
DATALIST = Factory.create_tag(TagTypeEnum.BODY, 'datalist', True)
OUTPUT = Factory.create_tag(TagTypeEnum.BODY, 'output', True)

# frame
IFRAME = Factory.create_tag(TagTypeEnum.BODY, 'iframe', True)

# image
IMG = Factory.create_tag(TagTypeEnum.BODY, 'img', False)
CANVAS = Factory.create_tag(TagTypeEnum.BODY, 'canvas', True)
FIGURE = Factory.create_tag(TagTypeEnum.BODY, 'figure', True)

# audio / video
AUDIO = Factory.create_tag(TagTypeEnum.BODY, 'audio', True)
VIDEO = Factory.create_tag(TagTypeEnum.BODY, 'video', True)

# link
A = Factory.create_tag(TagTypeEnum.BODY, 'a', True)
LINK_HEAD = Factory.create_tag(TagTypeEnum.HEAD, 'link', False)
LINK_BODY = Factory.create_tag(TagTypeEnum.BODY, 'link', False)
NAV = Factory.create_tag(TagTypeEnum.BODY, 'nav', True)

# list
UL = Factory.create_tag(TagTypeEnum.BODY, 'ul', True)
OL = Factory.create_tag(TagTypeEnum.BODY, 'ol', True)
IL = Factory.create_tag(TagTypeEnum.BODY, 'il', True)

# tables
TABLE = Factory.create_tag(TagTypeEnum.BODY, 'table', True)
TH = Factory.create_tag(TagTypeEnum.BODY, 'th', True)
TR = Factory.create_tag(TagTypeEnum.BODY, 'tr', True)
TD = Factory.create_tag(TagTypeEnum.BODY, 'td', True)
THEAD = Factory.create_tag(TagTypeEnum.BODY, 'thead', True)
TBODY = Factory.create_tag(TagTypeEnum.BODY, 'tbody', True)
TFOOT = Factory.create_tag(TagTypeEnum.BODY, 'tfoot', True)

# style
STYLE_HEAD = Factory.create_tag(TagTypeEnum.HEAD, 'style', True)
STYLE_BODY = Factory.create_tag(TagTypeEnum.BODY, 'style', True)
DIV = Factory.create_tag(TagTypeEnum.BODY, 'div', True)
SPAN = Factory.create_tag(TagTypeEnum.BODY, 'span', True)
HEADER = Factory.create_tag(TagTypeEnum.BODY, 'header', True)
FOOTER = Factory.create_tag(TagTypeEnum.BODY, 'footer', True)
MAIN = Factory.create_tag(TagTypeEnum.BODY, 'main', True)
SECTION = Factory.create_tag(TagTypeEnum.BODY, 'section', True)
ARTICLE = Factory.create_tag(TagTypeEnum.BODY, 'article', True)
ASIDE = Factory.create_tag(TagTypeEnum.BODY, 'aside', True)
DETAILS = Factory.create_tag(TagTypeEnum.BODY, 'details', True)
DIALOG = Factory.create_tag(TagTypeEnum.BODY, 'dialog', True)
SUMMARY = Factory.create_tag(TagTypeEnum.BODY, 'summary', True)
DATA = Factory.create_tag(TagTypeEnum.BODY, 'data', True)

# meta
META = Factory.create_tag(TagTypeEnum.HEAD, 'meta', False)

# programming
SCRIPT_HEAD = Factory.create_tag(TagTypeEnum.HEAD, 'script', True)
SCRIPT_BODY = Factory.create_tag(TagTypeEnum.BODY, 'script', True)
