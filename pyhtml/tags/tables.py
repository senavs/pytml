from ..dtypes.factory import BaseFactory

TABLE = BaseFactory.create_body_tag_class('table', True)
CAPTION = BaseFactory.create_body_tag_class('caption', True)
TH = BaseFactory.create_body_tag_class('th', True)
TR = BaseFactory.create_body_tag_class('tr', True)
TD = BaseFactory.create_body_tag_class('td', True)
THEAD = BaseFactory.create_body_tag_class('thead', True)
TBODY = BaseFactory.create_body_tag_class('tbody', True)
TFOOT = BaseFactory.create_body_tag_class('tfoot', True)
COL = BaseFactory.create_body_tag_class('col', False)
COLGROUP = BaseFactory.create_body_tag_class('colgroup', True)
