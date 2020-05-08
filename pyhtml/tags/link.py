from ..dtypes.factory import BaseFactory

A = BaseFactory.create_body_tag_class('a', True)
LINK = BaseFactory.create_body_tag_class('link', False)
NAV = BaseFactory.create_body_tag_class('nav', True)
