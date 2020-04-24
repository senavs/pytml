from typing import Union, List

from pyhtml.base.tags import Tag, BodyTag, HeadTag


class STYLE(HeadTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('style', inner, True, **arguments)


class DIV(BodyTag):

    def __init__(self, inner: Union[str, Tag, List[Tag]], **arguments):
        super().__init__('div', inner, True, **arguments)


class SPAN(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('span', inner, True, **arguments)


class HEADER(BodyTag):

    def __init__(self, inner: Union[str, Tag, List[Tag]], **arguments):
        super().__init__('header', inner, True, **arguments)


class FOOTER(BodyTag):

    def __init__(self, inner: Union[str, Tag, List[Tag]], **arguments):
        super().__init__('footer', inner, True, **arguments)


class MAIN(BodyTag):

    def __init__(self, inner: Union[str, Tag, List[Tag]], **arguments):
        super().__init__('main', inner, True, **arguments)


class SECTION(BodyTag):

    def __init__(self, inner: Union[str, Tag, List[Tag]], **arguments):
        super().__init__('section', inner, True, **arguments)


class ARTICLE(BodyTag):

    def __init__(self, inner: Union[str, Tag, List[Tag]], **arguments):
        super().__init__('article', inner, True, **arguments)


class ASIDE(BodyTag):

    def __init__(self, inner: Union[str, Tag, List[Tag]], **arguments):
        super().__init__('aside', inner, True, **arguments)


class DETAILS(BodyTag):

    def __init__(self, inner: Union[str, Tag, List[Tag]], **arguments):
        super().__init__('details', inner, True, **arguments)


class DIALOG(BodyTag):

    def __init__(self, inner: Union[str, Tag, List[Tag]], **arguments):
        super().__init__('dialog', inner, True, **arguments)


class SUMMARY(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('summary', inner, True, **arguments)


class DATA(BodyTag):

    def __init__(self, inner: Union[str], **arguments):
        super().__init__('data', inner, True, **arguments)
