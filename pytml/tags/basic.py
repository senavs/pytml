from typing import Union, List

from ..essential.tag import Tag, HeadTag, BodyTag


class HTML(Tag):

    def __init__(self, inner: Union[Tag, List[Tag]], **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, **kwargs)


class HEAD(Tag):

    def __init__(self, inner: Union[Tag, List[Tag]], **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, **kwargs)


class BODY(Tag):

    def __init__(self, inner: Union[str, Tag, List[Tag]], id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


class DIV(Tag, BodyTag):

    def __init__(self, inner: Union[str, Tag, List[Tag]], id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


class TITLE(Tag, HeadTag):

    def __init__(self, inner: str, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, **kwargs)


class H1(Tag, BodyTag):

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


class H2(Tag, BodyTag):

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


class H3(Tag, BodyTag):

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


class H4(Tag, BodyTag):

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


class H5(Tag, BodyTag):

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


class H6(Tag, BodyTag):

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


class META(Tag, HeadTag):

    def __init__(self, charset: str, **kwargs):
        name = self.__class__.__name__.lower()
        kwargs.update(charset=charset)
        super().__init__(name, '', False, **kwargs)


class BR(Tag, BodyTag):

    def __init__(self, **kwargs):
        super().__init__('br', '', False, **kwargs)


class HR(Tag, BodyTag):

    def __init__(self, **kwargs):
        super().__init__('hr', '', False, **kwargs)


class P(Tag, BodyTag):

    def __init__(self, inner: Union[str, Tag], id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


class COMMENT(Tag, BodyTag):

    def __init__(self, inner: str):
        self.tag = '<{name}{inner}-->'
        super().__init__('!--', inner, False)
