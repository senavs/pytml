from typing import Union, Tuple, Dict

from ..dtypes.base import Element, HeadTag, BodyTag, NotRecordableTag


class BaseFactory:

    @staticmethod
    def create_element_class():
        return Element()

    @staticmethod
    def create_head_tag_class(name: str, is_closed: bool):
        return HeadTag(name, is_closed)

    @staticmethod
    def create_body_tag_class(name: str, is_closed: bool):
        return BodyTag(name, is_closed)

    @staticmethod
    def create_not_recordable_tag_class(name: str, is_closed: bool):
        return NotRecordableTag(name, is_closed)
