from typing import Union, List

from ...base.tags import Tag, BodyTag, HeadTag
from ...base.register import Register


@Register
class STYLE(HeadTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('style', inner, True, **arguments)


@Register
class DIV(BodyTag):

    def __init__(self, inner: Union[str, Tag, List[Tag]], **arguments):
        super().__init__('div', inner, True, **arguments)


@Register
class SPAN(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('span', inner, True, **arguments)


@Register
class HEADER(BodyTag):

    def __init__(self, inner: Union[str, Tag, List[Tag]], **arguments):
        super().__init__('header', inner, True, **arguments)


@Register
class FOOTER(BodyTag):

    def __init__(self, inner: Union[str, Tag, List[Tag]], **arguments):
        super().__init__('footer', inner, True, **arguments)


@Register
class MAIN(BodyTag):

    def __init__(self, inner: Union[str, Tag, List[Tag]], **arguments):
        super().__init__('main', inner, True, **arguments)


@Register
class SECTION(BodyTag):

    def __init__(self, inner: Union[str, Tag, List[Tag]], **arguments):
        super().__init__('section', inner, True, **arguments)


@Register
class ARTICLE(BodyTag):

    def __init__(self, inner: Union[str, Tag, List[Tag]], **arguments):
        super().__init__('article', inner, True, **arguments)


@Register
class ASIDE(BodyTag):

    def __init__(self, inner: Union[str, Tag, List[Tag]], **arguments):
        super().__init__('aside', inner, True, **arguments)


@Register
class DETAILS(BodyTag):

    def __init__(self, inner: Union[str, Tag, List[Tag]], **arguments):
        super().__init__('details', inner, True, **arguments)


@Register
class DIALOG(BodyTag):

    def __init__(self, inner: Union[str, Tag, List[Tag]], **arguments):
        super().__init__('dialog', inner, True, **arguments)


@Register
class SUMMARY(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('summary', inner, True, **arguments)


@Register
class DATA(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('data', inner, True, **arguments)
