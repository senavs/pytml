from typing import Union, List

from ...base.tags import Tag, BodyTag
from ...base.register import Register


@Register
class UL(BodyTag):

    def __init__(self, inner: Union[Tag, List[Tag]], **arguments):
        super().__init__('ul', inner, True, **arguments)


@Register
class OL(BodyTag):

    def __init__(self, inner: Union[Tag, List[Tag]], **arguments):
        super().__init__('ol', inner, True, **arguments)


@Register
class LI(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('li', inner, True, **arguments)


@Register
class DL(BodyTag):

    def __init__(self, inner: Union[Tag, List[Tag]], **arguments):
        super().__init__('dl', inner, True, **arguments)


@Register
class DT(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('dt', inner, True, **arguments)


@Register
class DD(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('dd', inner, True, **arguments)
