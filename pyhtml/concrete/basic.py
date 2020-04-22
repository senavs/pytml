from typing import Union, List

from pyhtml.product.tag import Tag


class DOCTYPE(Tag):

    def __init__(self, inner: Union[Tag]):
        super().__init__('!DOCTYPE html', None, inner, False)


class HTML(Tag):

    def __init__(self, inner: Union['Tag', List['Tag']]):
        super().__init__('html', None, inner, True)


class HEAD(Tag):

    def __init__(self, inner: Union['Tag', List['Tag']]):
        super().__init__('head', None, inner, True)


class TITLE(Tag):

    def __init__(self, inner: Union[str]):
        super().__init__('title', None, inner, True)


class BODY(Tag):

    def __init__(self, arguments: Union[None, dict], inner: Union[str, 'Tag', List['Tag']]):
        super().__init__('body', arguments, inner, True)


class H1(Tag):

    def __init__(self, arguments: Union[None, dict], inner: Union[str]):
        super().__init__('h1', arguments, inner, True)


class H2(Tag):

    def __init__(self, arguments: Union[None, dict], inner: Union[str]):
        super().__init__('h2', arguments, inner, True)


class H3(Tag):

    def __init__(self, arguments: Union[None, dict], inner: Union[str]):
        super().__init__('h3', arguments, inner, True)


class H4(Tag):

    def __init__(self, arguments: Union[None, dict], inner: Union[str]):
        super().__init__('h4', arguments, inner, True)


class H5(Tag):

    def __init__(self, arguments: Union[None, dict], inner: Union[str]):
        super().__init__('h5', arguments, inner, True)


class H6(Tag):

    def __init__(self, arguments: Union[None, dict], inner: Union[str]):
        super().__init__('h6', arguments, inner, True)


class P(Tag):

    def __init__(self, arguments: Union[None, dict], inner: Union[str]):
        super().__init__('p', arguments, inner, True)


class BR(Tag):

    def __init__(self):
        super().__init__('p', None, None, False)


class HR(Tag):

    def __init__(self):
        super().__init__('p', None, None, False)
