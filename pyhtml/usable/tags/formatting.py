from typing import Union, List

from ...base.tags import Tag, BodyTag
from ...base.register import Register


@Register
class ABBR(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('abbr', inner, True, **arguments)


@Register
class ADDRESS(BodyTag):

    def __init__(self, inner: Union[str, 'Tag', List['Tag']], **arguments):
        super().__init__('address', inner, True, **arguments)


@Register
class DBI(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('bdi', inner, True, **arguments)


@Register
class DBO(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('bdo', inner, True, **arguments)


@Register
class BLOCKQUOTE(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('blockquote', inner, True, **arguments)


@Register
class CITE(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('cite', inner, True, **arguments)


@Register
class CODE(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('code', inner, True, **arguments)


@Register
class DEL(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('del', inner, True, **arguments)


@Register
class DFN(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('dfn', inner, True, **arguments)


@Register
class EM(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('em', inner, True, **arguments)


@Register
class I(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('i', inner, True, **arguments)


@Register
class INS(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('ins', inner, True, **arguments)


@Register
class KDB(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('kdb', inner, True, **arguments)


@Register
class MARK(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('mark', inner, True, **arguments)


@Register
class METER(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('meter', inner, True, **arguments)


@Register
class PROGRESS(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('progress', inner, True, **arguments)


@Register
class Q(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('q', inner, True, **arguments)


@Register
class S(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('s', inner, True, **arguments)


@Register
class SAMP(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('samp', inner, True, **arguments)


@Register
class SMALL(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('small', inner, True, **arguments)


@Register
class STRONG(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('strong', inner, True, **arguments)


@Register
class SUB(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('sub', inner, True, **arguments)


@Register
class SUP(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('sup', inner, True, **arguments)


@Register
class TEMPLATE(BodyTag):

    def __init__(self, inner: Union[str, Tag, List['Tag']], **arguments):
        super().__init__('template', inner, True, **arguments)


@Register
class TIME(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('time', inner, True, **arguments)


@Register
class U(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('u', inner, True, **arguments)


@Register
class VARIABLE(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('variable', inner, True, **arguments)
