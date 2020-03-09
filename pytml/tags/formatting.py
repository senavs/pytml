from typing import Union

from ..essential.tag import Tag


class B(Tag):

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


class CODE(Tag):

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


class MARK(Tag):

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


class SMALL(Tag):

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


class STRONG(Tag):

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


class I(Tag):

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)
