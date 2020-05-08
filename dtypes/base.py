from typing import Union, List


class Element:
    _element_fmr = '{inner}'
    __inner = ''

    def __init__(self, inner: Union[str, 'Element', List['Element']]):
        self.inner = inner

    @property
    def inner(self):
        return self.__inner

    @inner.setter
    def inner(self, elements: Union[str, 'Element', List['Element']]):
        if isinstance(elements, Element):
            self.__inner = elements.render()
        if isinstance(elements, List):
            self.__inner = ''.join(element.render() for element in elements)
        else:
            self.__inner = elements

    def render(self) -> str:
        return self._element_fmr.format(inner=self.inner)

    def __str__(self):
        return self.render()


class Tag(Element):
    _element_fmr = '<{name}{attributes}>{inner}'
    __name = __attributes = ''

    def __init__(self, name: str, inner: Union[str, 'Element', List['Element']], is_closed: bool, **kwargs):
        super().__init__(inner)
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

    def render(self) -> str:
        return self._element_fmr.format(name=self.name, attributes=self.attributes, inner=self.inner)
