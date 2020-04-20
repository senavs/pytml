from typing import Union, List


class Tag:
    __tag_format = '<{name}{arguments}>{inner}'
    __name = __arguments = __inner = ''

    def __init__(self, name: str, arguments: Union[None, dict], inner: Union[None, str, 'Tag', List['Tag']], is_closed: bool):
        self.name = name
        self.arguments = arguments
        self.inner = inner

        if is_closed:
            self.__tag_format += f'</{self.name}>'

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def arguments(self) -> str:
        return self.__arguments

    @arguments.setter
    def arguments(self, arguments: dict):
        if arguments:
            for key, value in arguments.items():
                self.__arguments += f' {key}="{value}"'

    @property
    def inner(self) -> str:
        return self.__inner

    @inner.setter
    def inner(self, elements: Union[str, 'Tag', List['Tag']]):
        if elements:
            if isinstance(elements, Tag):
                self.__inner = elements.render()
            elif isinstance(elements, List):
                self.__inner = ''.join(element.render() for element in elements)
            else:
                self.__inner = elements

    def render(self):
        return self.__tag_format.format(name=self.name, arguments=self.arguments, inner=self.inner)

    def __repr__(self):
        return self.render()
