from typing import Union, List


class Tag:
    _name = _arguments = _inner = ''
    _is_closed = False
    tag = '<{name}{arguments}>{inner}'

    def __init__(self, name: str, inner: Union[str, 'Tag', List['Tag']], is_closed: bool, **kwargs):
        self.name = name
        self.inner = inner
        self.is_close = is_closed
        self.arguments = kwargs

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = str(value)

    @property
    def arguments(self) -> str:
        """Get tag arguments"""
        return self._arguments

    @arguments.setter
    def arguments(self, values: dict):
        """Set tag arguments"""
        args = ''
        for key, value in values.items():
            args += f' {str(key)}="{str(value)}"'
        else:
            self._arguments = args

    @property
    def inner(self) -> str:
        """Get inner html"""
        return self._inner

    @inner.setter
    def inner(self, elements: Union[str, 'Tag', List['Tag']]):
        """Set inner html"""
        inner_html = ''
        if isinstance(elements, Tag):
            inner_html = elements.render()
        elif isinstance(elements, List):
            inner_html = ''.join(element.render() for element in elements)
        else:
            inner_html = str(elements)
        self._inner = inner_html

    @property
    def is_close(self) -> bool:
        """Get close tag </x> if the tag is closed"""
        return self._is_closed

    @is_close.setter
    def is_close(self, closed: bool):
        """Set close tag </x> if the tag is closed"""
        if closed:
            self.tag += '</{name}>'
            self._is_closed = True

    def render(self) -> str:
        """Transform Tag class in HTML tag string"""
        return self.tag.format(name=self.name, arguments=self.arguments, inner=self.inner)

    def __repr__(self) -> str:
        return self.render()
