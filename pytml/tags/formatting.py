from typing import Union

<<<<<<< HEAD
from ..essential.tag import Tag, BodyTag


class B(Tag, BodyTag):
=======
from ..essential.tag import Tag


class B(Tag):
>>>>>>> 2ac40b6... Tags

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


<<<<<<< HEAD
class CODE(Tag, BodyTag):
=======
class CODE(Tag):
>>>>>>> 2ac40b6... Tags

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


<<<<<<< HEAD
class MARK(Tag, BodyTag):
=======
class MARK(Tag):
>>>>>>> 2ac40b6... Tags

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


<<<<<<< HEAD
class SMALL(Tag, BodyTag):
=======
class SMALL(Tag):
>>>>>>> 2ac40b6... Tags

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


<<<<<<< HEAD
class STRONG(Tag, BodyTag):
=======
class STRONG(Tag):
>>>>>>> 2ac40b6... Tags

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


<<<<<<< HEAD
class I(Tag, BodyTag):
=======
class I(Tag):
>>>>>>> 2ac40b6... Tags

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)
