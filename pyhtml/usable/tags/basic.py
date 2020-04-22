from typing import Union, List

from pyhtml.base.tags import Tag, HeadTag, BodyTag, UnrecordableTag


class DOCTYPE(UnrecordableTag):

    def __init__(self, inner: Union[Tag]):
        super().__init__('!DOCTYPE html', inner, False)


class HTML(UnrecordableTag):

    def __init__(self, inner: Union['Tag', List['Tag']]):
        super().__init__('html', inner, True)


class HEAD(UnrecordableTag):

    def __init__(self, inner: Union['Tag', List['Tag']]):
        super().__init__('head', inner, True)


class TITLE(HeadTag):

    def __init__(self, inner: Union[str]):
        super().__init__('title', inner, True)


class META(HeadTag):

    def __init__(self, **arguments):
        super().__init__('title', None, True, **arguments)


class BODY(UnrecordableTag):

    def __init__(self, inner: Union[str, 'Tag', List['Tag']], **arguments):
        super().__init__('body', inner, True, **arguments)


class H1(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('h1', inner, True, **arguments)


class H2(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('h2', inner, True, **arguments)


class H3(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('h3', inner, True, **arguments)


class H4(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('h4', inner, True, **arguments)


class H5(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('h5', inner, True, **arguments)


class H6(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('h6', inner, True, **arguments)


class P(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('p', inner, True, **arguments)


class BR(BodyTag):

    def __init__(self):
        super().__init__('p', None, False)


class HR(BodyTag):

    def __init__(self):
        super().__init__('p', None, False)
