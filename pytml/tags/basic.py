from typing import Union, List

<<<<<<< HEAD
from ..essential.tag import Tag, HeadTag, BodyTag
=======
from ..essential.tag import Tag
>>>>>>> 2ac40b6... Tags


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


<<<<<<< HEAD
class DIV(Tag, BodyTag):
=======
class DIV(Tag):
>>>>>>> 2ac40b6... Tags

    def __init__(self, inner: Union[str, Tag, List[Tag]], id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


<<<<<<< HEAD
class TITLE(Tag, HeadTag):
=======
class TITLE(Tag):
>>>>>>> 2ac40b6... Tags

    def __init__(self, inner: str, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, **kwargs)


<<<<<<< HEAD
class H1(Tag, BodyTag):
=======
class H1(Tag):
>>>>>>> 2ac40b6... Tags

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


<<<<<<< HEAD
class H2(Tag, BodyTag):
=======
class H2(Tag):
>>>>>>> 2ac40b6... Tags

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


<<<<<<< HEAD
class H3(Tag, BodyTag):
=======
class H3(Tag):
>>>>>>> 2ac40b6... Tags

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


<<<<<<< HEAD
class H4(Tag, BodyTag):
=======
class H4(Tag):
>>>>>>> 2ac40b6... Tags

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


<<<<<<< HEAD
class H5(Tag, BodyTag):
=======
class H5(Tag):
>>>>>>> 2ac40b6... Tags

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


<<<<<<< HEAD
class H6(Tag, BodyTag):
=======
class H6(Tag):
>>>>>>> 2ac40b6... Tags

    def __init__(self, inner: str, id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


<<<<<<< HEAD
class META(Tag, HeadTag):
=======
class META(Tag):
>>>>>>> 2ac40b6... Tags

    def __init__(self, charset: str, **kwargs):
        name = self.__class__.__name__.lower()
        kwargs.update(charset=charset)
        super().__init__(name, '', False, **kwargs)


<<<<<<< HEAD
class BR(Tag, BodyTag):
=======
class BR(Tag):
>>>>>>> 2ac40b6... Tags

    def __init__(self, **kwargs):
        super().__init__('br', '', False, **kwargs)


<<<<<<< HEAD
class HR(Tag, BodyTag):
=======
class HR(Tag):
>>>>>>> 2ac40b6... Tags

    def __init__(self, **kwargs):
        super().__init__('hr', '', False, **kwargs)


<<<<<<< HEAD
class P(Tag, BodyTag):
=======
class P(Tag):
>>>>>>> 2ac40b6... Tags

    def __init__(self, inner: Union[str, Tag], id_: str = None, class_: str = None, **kwargs):
        name = self.__class__.__name__.lower()
        super().__init__(name, inner, True, id_, class_, **kwargs)


<<<<<<< HEAD
class COMMENT(Tag, BodyTag):
=======
class COMMENT(Tag):
>>>>>>> 2ac40b6... Tags

    def __init__(self, inner: str):
        self.tag = '<{name}{inner}-->'
        super().__init__('!--', inner, False)
