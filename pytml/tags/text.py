from ..essential.tag import Tag


class H1(Tag):

    def __init__(self, inner: str, **kwargs):
        super().__init__('h1', inner, True, **kwargs)


class H2(Tag):

    def __init__(self, inner: str, **kwargs):
        super().__init__('h2', inner, True, **kwargs)


class H3(Tag):

    def __init__(self, inner: str, **kwargs):
        super().__init__('h3', inner, True, **kwargs)


class H4(Tag):

    def __init__(self, inner: str, **kwargs):
        super().__init__('h4', inner, True, **kwargs)


class H5(Tag):

    def __init__(self, inner: str, **kwargs):
        super().__init__('h5', inner, True, **kwargs)


class H6(Tag):

    def __init__(self, inner: str, **kwargs):
        super().__init__('h6', inner, True, **kwargs)


class B(Tag):

    def __init__(self, inner: str, **kwargs):
        super().__init__('b', inner, True, **kwargs)


class I(Tag):

    def __init__(self, inner: str, **kwargs):
        super().__init__('i', inner, True, **kwargs)


class P(Tag):

    def __init__(self, inner: str, **kwargs):
        super().__init__('p', inner, True, **kwargs)


class TITLE(Tag):

    def __init__(self, inner: str, **kwargs):
        super().__init__('title', inner, True, **kwargs)


class MARK(Tag):

    def __init__(self, inner: str, **kwargs):
        super().__init__('mark', inner, True, **kwargs)


class SMALL(Tag):

    def __init__(self, inner: str, **kwargs):
        super().__init__('small', inner, True, **kwargs)


class STRONG(Tag):

    def __init__(self, inner: str, **kwargs):
        super().__init__('strong', inner, True, **kwargs)
