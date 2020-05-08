from typing import Union, List


class Element:
    _element_fmr = '{inner}'
    _loaded = False
    __inner = ''

    @property
    def inner(self):
        return self.__inner

    @inner.setter
    def inner(self, elements: Union[None, str, 'Element', List['Element']]):
        if elements:
            if isinstance(elements, Element):
                self.__inner = elements.compile()
            if isinstance(elements, List):
                self.__inner = ''.join(elements)
            else:
                self.__inner = elements
        else:
            self.__inner = ''

    def compile(self) -> str:
        if self._loaded:
            return self._element_fmr.format(inner=self.inner)
        raise RuntimeError('Element was not loaded yet')

    def __call__(self, inner: Union[None, str, 'Element', List['Element']] = None):
        self.inner = inner
        self._loaded = True
        return self.compile()


class Tag(Element):
    _element_fmr = '<{name}{attributes}>{inner}'
    __name = __attributes = ''

    def __init__(self, name: str, is_closed: bool, **kwargs):
        if is_closed:
            self._element_fmr += '</{name}>'

        self.name = name
        self.attributes = kwargs

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def attributes(self) -> str:
        return self.__attributes

    @attributes.setter
    def attributes(self, kwargs: dict):
        if kwargs:
            for key, value in kwargs.items():
                if str(key).endswith('_'):
                    key = key[:-1]
                self.__attributes += f' {key}="{value}"'

    def compile(self) -> str:
        if self._loaded:
            return self._element_fmr.format(name=self.name, attributes=self.attributes, inner=self.inner)
        raise RuntimeError('Element was not loaded yet')

    def __call__(self, inner: Union[None, str, 'Element', List['Element']] = None, **kwargs):
        self.inner = inner
        self.attributes = kwargs
        self._loaded = True
        return self.compile()


class HeadTag(Tag):
    """Class to identify head tags"""


class BodyTag(Tag):
    """Class to identify body tags"""


class NotRecordableTag(Tag):
    """Class to identify not recordable tags"""
