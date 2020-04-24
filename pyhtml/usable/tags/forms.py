from typing import Union, List

from ...base.tags import Tag, BodyTag
from ...base.register import Register


@Register
class FORM(BodyTag):

    def __init__(self, inner: Union[Tag, List[Tag]], **arguments):
        super().__init__('form', inner, True, **arguments)


@Register
class INPUT(BodyTag):

    def __init__(self, **arguments):
        super().__init__('input', None, False, **arguments)


@Register
class TEXTAREA(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('textarea', inner, True, **arguments)


@Register
class BUTTON(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('button', inner, True, **arguments)


@Register
class SELECT(BodyTag):

    def __init__(self, inner: Union[Tag, List[Tag]], **arguments):
        super().__init__('select', inner, True, **arguments)


@Register
class OPTGROUP(BodyTag):

    def __init__(self, inner: Union[Tag, List[Tag]], **arguments):
        super().__init__('optgroup', inner, True, **arguments)


@Register
class OPTION(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('option', inner, True, **arguments)


@Register
class LABEL(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('label', inner, True, **arguments)


@Register
class FIELDSET(BodyTag):

    def __init__(self, inner: Union[str, Tag, List[Tag]], **arguments):
        super().__init__('fieldset', inner, True, **arguments)


@Register
class LEGEND(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('legend', inner, True, **arguments)


@Register
class DATALIST(BodyTag):

    def __init__(self, inner: Union[Tag, List[Tag]], **arguments):
        super().__init__('datalist', inner, True, **arguments)


@Register
class OUTPUT(BodyTag):

    def __init__(self, inner: Union[Tag, List[Tag]], **arguments):
        super().__init__('output', inner, True, **arguments)
