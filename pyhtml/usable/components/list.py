from typing import Union, Tuple

from ...base.component import Component
from ...usable.tags.list import LI


class OrderedList(Component):
    """Ordered List class"""

    def __init__(self, *datas: Union[str, Tuple[str, dict]], **arguments):
        """
        Parameters
        *data (str): data that will be placed in <li> tags
        *data (Tuple[str, dict]): data that will be placed in <li> tags and its arguments
        **arguments: <ol> arguments
        """
        inner = []
        for data in datas:
            if isinstance(data, tuple):
                tag = LI(data[0], **data[1])
            else:
                tag = LI(data)
            inner.append(tag)
        super().__init__('ol', inner, **arguments)


class UnorderedList(Component):
    """Unordered List class"""

    def __init__(self, *datas: Union[str, Tuple[str, dict]], **arguments):
        """
        Parameters
        *data (str): data that will be placed in <li> tags
        *data (Tuple[str, dict]): data that will be placed in <li> tags and its arguments
        **arguments: <ul> arguments
        """
        inner = []
        for data in datas:
            if isinstance(data, tuple):
                tag = LI(data[0], **data[1])
            else:
                tag = LI(data)
            inner.append(tag)
        super().__init__('ul', inner, **arguments)
