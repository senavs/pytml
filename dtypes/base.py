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
