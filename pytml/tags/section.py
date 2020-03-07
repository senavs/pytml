from typing import Union, List

from ..essential.tag import Tag


class HTML(Tag):

    def __init__(self, inner: Union[Tag, List[Tag]], **kwargs):
        super().__init__('html', inner, True, **kwargs)


class HEAD(Tag):

    def __init__(self, inner: Union[Tag, List[Tag]], **kwargs):
        super().__init__('head', inner, True, **kwargs)


class BODY(Tag):

    def __init__(self, inner: Union[str, Tag, List[Tag]], **kwargs):
        super().__init__('body', inner, True, **kwargs)


class DIV(Tag):

    def __init__(self, inner: Union[str, Tag, List[Tag]], **kwargs):
        super().__init__('div', inner, True, **kwargs)
