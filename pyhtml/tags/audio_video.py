from ..dtypes.factory import BaseFactory

AUDIO = BaseFactory.create_body_tag_class('audio', True)
SOURCE = BaseFactory.create_body_tag_class('source', False)
TRACK = BaseFactory.create_body_tag_class('track', False)
VIDEO = BaseFactory.create_body_tag_class('video', True)
