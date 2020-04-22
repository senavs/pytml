from typing import Union, List

from pyhtml.base.tags import Tag, BodyTag


class ABBR(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('abbr', inner, True, **arguments)


class ADDRESS(BodyTag):

    def __init__(self, inner: Union[str, 'Tag', List['Tag']], **arguments):
        super().__init__('address', inner, True, **arguments)


class DBI(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('bdi', inner, True, **arguments)


class DBO(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('bdo', inner, True, **arguments)


class BLOCKQUOTE(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('blockquote', inner, True, **arguments)


class CITE(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('cite', inner, True, **arguments)


class CODE(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('code', inner, True, **arguments)


class DEL(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('del', inner, True, **arguments)


class DFN(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('dfn', inner, True, **arguments)


class EM(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('em', inner, True, **arguments)


class I(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('i', inner, True, **arguments)


class INS(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('ins', inner, True, **arguments)


class KDB(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('kdb', inner, True, **arguments)


class MARK(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('mark', inner, True, **arguments)


class METER(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('meter', inner, True, **arguments)


class PROGRESS(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('progress', inner, True, **arguments)


class Q(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('q', inner, True, **arguments)


class S(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('s', inner, True, **arguments)


class SAMP(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('samp', inner, True, **arguments)


class SMALL(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('small', inner, True, **arguments)


class STRONG(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('strong', inner, True, **arguments)


class SUB(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('sub', inner, True, **arguments)


class SUP(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('sup', inner, True, **arguments)


class TEMPLATE(BodyTag):

    def __init__(self, inner: Union[str, Tag, List['Tag']], **arguments):
        super().__init__('template', inner, True, **arguments)


class TIME(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('time', inner, True, **arguments)


class U(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('u', inner, True, **arguments)


class VARIABLE(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('variable', inner, True, **arguments)
