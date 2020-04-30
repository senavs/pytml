from typing import Union, List

from ...base.tags import BodyTag, Tag
from ...base.register import Register


@Register
class LINK(BodyTag):

    def __init__(self, **arguments):
        super().__init__('link', None, False, **arguments)


@Register
class A(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('a', inner, True, **arguments)


@Register
class NAV(BodyTag):

    def __init__(self, inner: Union[str, Tag, List[Tag]], **arguments):
        super().__init__('nav', inner, True, **arguments)
