from ..dtypes.factory import BaseFactory

IMG = BaseFactory.create_body_tag_class('img', False)
MAP = BaseFactory.create_body_tag_class('map', True)
AREA = BaseFactory.create_body_tag_class('area', False)
CANVAS = BaseFactory.create_body_tag_class('canvas', True)
FIGCAPTION = BaseFactory.create_body_tag_class('figcaption', True)
FIGURE = BaseFactory.create_body_tag_class('figure', True)
PICTURE = BaseFactory.create_body_tag_class('picture', True)
SVG = BaseFactory.create_body_tag_class('svg', True)
