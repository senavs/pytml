from pyhtml.dtype.base import BaseElement, BaseTag, TagTypeEnum


class Factory:

    @classmethod
    def create_element(cls) -> BaseElement:
        return BaseElement()

    @classmethod
    def create_tag(cls, tag_type: TagTypeEnum, name: str, is_closed: bool) -> BaseTag:
        return tag_type.value(name, is_closed)
