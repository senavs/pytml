from typing import Union, List

from pyhtml.base.tags import Tag, BodyTag


class FORM(BodyTag):

    def __init__(self, inner: Union[Tag, List[Tag]], **arguments):
        super().__init__('form', inner, True, **arguments)


class INPUT(BodyTag):

    def __init__(self, **arguments):
        super().__init__('input', None, False, **arguments)


class TEXTAREA(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('textarea', inner, True, **arguments)


class BUTTON(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('button', inner, True, **arguments)


class SELECT(BodyTag):

    def __init__(self, inner: Union[Tag, List[Tag]], **arguments):
        super().__init__('select', inner, True, **arguments)


class OPTGROUP(BodyTag):

    def __init__(self, inner: Union[Tag, List[Tag]], **arguments):
        super().__init__('optgroup', inner, True, **arguments)


class OPTION(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('option', inner, True, **arguments)


class LABEL(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('label', inner, True, **arguments)


class FIELDSET(BodyTag):

    def __init__(self, inner: Union[str, Tag, List[Tag]], **arguments):
        super().__init__('fieldset', inner, True, **arguments)


class LEGEND(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('legend', inner, True, **arguments)


class DATALIST(BodyTag):

    def __init__(self, inner: Union[Tag, List[Tag]], **arguments):
        super().__init__('datalist', inner, True, **arguments)


class OUTPUT(BodyTag):

    def __init__(self, inner: Union[Tag, List[Tag]], **arguments):
        super().__init__('output', inner, True, **arguments)
