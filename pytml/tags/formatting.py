from typing import Union

<<<<<<< HEAD
<<<<<<< HEAD
from ..essential.tag import Tag, BodyTag


class B(Tag, BodyTag):
=======
from ..essential.tag import Tag


class B(Tag):
>>>>>>> 2ac40b6... Tags
=======
from ..essential.tag import Tag, BodyTag


class B(Tag, BodyTag):
>>>>>>> cc3787a... head and body tag classes

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


<<<<<<< HEAD
<<<<<<< HEAD
class CODE(Tag, BodyTag):
=======
class CODE(Tag):
>>>>>>> 2ac40b6... Tags
=======
class CODE(Tag, BodyTag):
>>>>>>> cc3787a... head and body tag classes

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


<<<<<<< HEAD
<<<<<<< HEAD
class MARK(Tag, BodyTag):
=======
class MARK(Tag):
>>>>>>> 2ac40b6... Tags
=======
class MARK(Tag, BodyTag):
>>>>>>> cc3787a... head and body tag classes

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


<<<<<<< HEAD
<<<<<<< HEAD
class SMALL(Tag, BodyTag):
=======
class SMALL(Tag):
>>>>>>> 2ac40b6... Tags
=======
class SMALL(Tag, BodyTag):
>>>>>>> cc3787a... head and body tag classes

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


<<<<<<< HEAD
<<<<<<< HEAD
class STRONG(Tag, BodyTag):
=======
class STRONG(Tag):
>>>>>>> 2ac40b6... Tags
=======
class STRONG(Tag, BodyTag):
>>>>>>> cc3787a... head and body tag classes

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


<<<<<<< HEAD
<<<<<<< HEAD
class I(Tag, BodyTag):
=======
class I(Tag):
>>>>>>> 2ac40b6... Tags
=======
class I(Tag, BodyTag):
>>>>>>> cc3787a... head and body tag classes

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)
