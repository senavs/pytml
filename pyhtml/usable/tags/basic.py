from typing import Union, List

from ...base.tags import Tag, HeadTag, BodyTag, UnrecordableTag
from ...base.register import Register


@Register
class DOCTYPE(UnrecordableTag):

    def __init__(self, inner: Union[Tag]):
        super().__init__('!DOCTYPE html', inner, False)


@Register
class HTML(UnrecordableTag):

    def __init__(self, inner: Union['Tag', List['Tag']]):
        super().__init__('html', inner, True)


@Register
class HEAD(UnrecordableTag):

    def __init__(self, inner: Union['Tag', List['Tag']]):
        super().__init__('head', inner, True)


@Register
class TITLE(HeadTag):

    def __init__(self, inner: Union[str]):
        super().__init__('title', inner, True)


@Register
class META(HeadTag):

    def __init__(self, **arguments):
        super().__init__('title', None, True, **arguments)


@Register
class BODY(UnrecordableTag):

    def __init__(self, inner: Union[str, 'Tag', List['Tag']], **arguments):
        super().__init__('body', inner, True, **arguments)


@Register
class H1(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('h1', inner, True, **arguments)


@Register
class H2(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('h2', inner, True, **arguments)


@Register
class H3(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('h3', inner, True, **arguments)


@Register
class H4(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('h4', inner, True, **arguments)


@Register
class H5(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('h5', inner, True, **arguments)


@Register
class H6(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('h6', inner, True, **arguments)


@Register
class P(BodyTag):

    def __init__(self, inner: Union[str, Tag, List['Tag']], **arguments):
        super().__init__('p', inner, True, **arguments)


@Register
class BR(BodyTag):

    def __init__(self):
        super().__init__('p', None, False)


@Register
class HR(BodyTag):

    def __init__(self):
        super().__init__('p', None, False)
