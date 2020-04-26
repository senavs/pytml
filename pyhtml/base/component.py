from typing import Union, Tuple, List

from pyhtml.base.tags import BodyTag, Tag


class Component(BodyTag):

    def __init__(self, inner: Union[Tag, List[Tag]], **arguments):
        super().__init__('div', inner, True, **arguments)
