from ..dtypes.factory import BaseFactory

SCRIPT_HEAD = BaseFactory.create_head_tag_class('script', True)
SCRIPT_BODY = BaseFactory.create_body_tag_class('script', True)
NOSCRIPT = BaseFactory.create_body_tag_class('noscript', True)
EMBED = BaseFactory.create_body_tag_class('embed', False)
OBJECT = BaseFactory.create_body_tag_class('object', False)
PARAM = BaseFactory.create_body_tag_class('param', False)
