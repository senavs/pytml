from pyhtml.dtype.base import HeadTag, BodyTag, UnallocatedTag

# base
HTML = UnallocatedTag('html', True)
HEAD = UnallocatedTag('head', True)
BODY = UnallocatedTag('body', True)
TITLE = HeadTag('title', True)
H1 = BodyTag('h1', True)
H2 = BodyTag('h2', True)
H3 = BodyTag('h3', True)
H4 = BodyTag('h4', True)
H5 = BodyTag('h5', True)
H6 = BodyTag('h6', True)
P = BodyTag('p', True)
BR = BodyTag('br', False)
HR = BodyTag('hr', False)

# formatting
ABBR = BodyTag('abbr', True)
ADDRESS = BodyTag('address', True)
B = BodyTag('b', True)
BLOCKQUOTE = BodyTag('blockquote', True)
CITE = BodyTag('cite', True)
CODE = BodyTag('code', True)
I = BodyTag('i', True)
MARK = BodyTag('mark', True)
PROGRESS = BodyTag('progress', True)
RUBY = BodyTag('ruby', True)
SAMP = BodyTag('samp', True)
SMALL = BodyTag('small', True)
STRONG = BodyTag('strong', True)
TEMPLATE = BodyTag('template', True)
TIME = BodyTag('time', True)
U = BodyTag('u', True)

# form
FORM = BodyTag('form', True)
INPUT = BodyTag('input', False)
TEXTAREA = BodyTag('textarea', True)
BUTTON = BodyTag('button', True)
SELECT = BodyTag('select', True)
OPTGROUP = BodyTag('optgroup', True)
OPTION = BodyTag('option', True)
LABEL = BodyTag('label', True)
FIELDSET = BodyTag('fieldset', True)
LEGEND = BodyTag('legend', True)
DATALIST = BodyTag('datalist', True)
OUTPUT = BodyTag('output', True)

# frame
IFRAME = BodyTag('iframe', True)

# image
IMG = BodyTag('img', False)
CANVAS = BodyTag('canvas', True)
FIGURE = BodyTag('figure', True)

# audio / video
AUDIO = BodyTag('audio', True)
VIDEO = BodyTag('video', True)

# link
A = BodyTag('a', True)
LINK_HEAD = HeadTag('link', False)
LINK_BODY = BodyTag('link', False)
NAV = BodyTag('nav', True)

# list
UL = BodyTag('ul', True)
OL = BodyTag('ol', True)
LI = BodyTag('li', True)

# tables
TABLE = BodyTag('table', True)
TH = BodyTag('th', True)
TR = BodyTag('tr', True)
TD = BodyTag('td', True)
THEAD = BodyTag('thead', True)
TBODY = BodyTag('tbody', True)
TFOOT = BodyTag('tfoot', True)

# style
STYLE_HEAD = HeadTag('style', True)
STYLE_BODY = BodyTag('style', True)
DIV = BodyTag('div', True)
SPAN = BodyTag('span', True)
HEADER = BodyTag('header', True)
FOOTER = BodyTag('footer', True)
MAIN = BodyTag('main', True)
SECTION = BodyTag('section', True)
ARTICLE = BodyTag('article', True)
ASIDE = BodyTag('aside', True)
DETAILS = BodyTag('details', True)
DIALOG = BodyTag('dialog', True)
SUMMARY = BodyTag('summary', True)
DATA = BodyTag('data', True)

# meta
META = HeadTag('meta', False)

# programming
SCRIPT_HEAD = HeadTag('script', True)
SCRIPT_BODY = BodyTag('script', True)
