from typing import Union, List

from essential.tag import Tag


class IMG(Tag):

    def __init__(self, inner: Union[str, Tag, List[Tag]], scr: str, **kwargs):
        kwargs.update(scr=scr)
        super().__init__('img', inner, False, **kwargs)


class A(Tag):

    def __init__(self, inner: Union[str, Tag, List[Tag]], href: str, **kwargs):
        kwargs.update(href=href)
        super().__init__('a', inner, True, **kwargs)
