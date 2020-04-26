from typing import Union, Tuple

from ...base.component import Component
from ...usable.tags.list import OL, UL, LI


class OrderedList(Component):

    def __init__(self, *datas: Union[str, Tuple[str, dict]], **arguments):
        inner = []
        for data in datas:
            if isinstance(data, tuple):
                tag = LI(data[0], **data[1])
            else:
                tag = LI(data)
            inner.append(tag)
        inner = OL(inner)
        super().__init__(inner, **arguments)


class UnorderedList(Component):

    def __init__(self, *datas: Union[str, Tuple[str, dict]], **arguments):
        inner = []
        for data in datas:
            if isinstance(data, tuple):
                tag = LI(data[0], **data[1])
            else:
                tag = LI(data)
            inner.append(tag)
        inner = UL(inner)
        super().__init__(inner, **arguments)
