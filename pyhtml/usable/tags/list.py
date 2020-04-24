from typing import Union, List

from pyhtml.base.tags import Tag, BodyTag


class UL(BodyTag):

    def __init__(self, inner: Union[Tag, List[Tag]], **arguments):
        super().__init__('ul', inner, True, **arguments)


class OL(BodyTag):

    def __init__(self, inner: Union[Tag, List[Tag]], **arguments):
        super().__init__('ol', inner, True, **arguments)


class LI(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('li', inner, True, **arguments)


class DL(BodyTag):

    def __init__(self, inner: Union[Tag, List[Tag]], **arguments):
        super().__init__('dl', inner, True, **arguments)


class DT(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('dt', inner, True, **arguments)


class DD(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('dd', inner, True, **arguments)
