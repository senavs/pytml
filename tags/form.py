from typing import Union, List

from essential.tag import Tag


class FORM(Tag):

    def __init__(self, inner: Union[Tag, List[Tag]], action: str, method: str, **kwargs):
        kwargs.update(action=action, method=method)
        super().__init__('form', inner, True, **kwargs)


class LABEL(Tag):

    def __init__(self, inner: str, for_: str, **kwargs):
        kwargs.update({'for': for_})
        super().__init__('label', inner, True, **kwargs)


class INPUT(Tag):

    def __init__(self, type: str, name: str, **kwargs):
        kwargs.update(type=type, name=name)
        super().__init__('input', '', False, **kwargs)


class BUTTON(Tag):

    def __init__(self, inner: str, type: str, **kwargs):
        kwargs.update(type=type)
        super().__init__('button', inner, True, **kwargs)


class NAV(Tag):

    def __init__(self, inner: Union[Tag, List[Tag]], action: str, method: str, **kwargs):
        kwargs.update(action=action, method=method)
        super().__init__('nav', inner, True, **kwargs)
