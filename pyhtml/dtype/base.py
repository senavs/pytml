from typing import Union, MutableSequence


class BaseElement:
    _inner = ''
    _format = '{inner}'

    @staticmethod
    def set_inner(value: Union[None, 'BaseElement', MutableSequence['BaseElement']] = None):
        if value:
            inner = ''
            if isinstance(value, str):
                inner = value
            elif isinstance(value, BaseElement):
                inner = value.compile()
            elif isinstance(value, MutableSequence):
                inner = ''.join(element.compile() for element in value)

            return inner

    def copy(self) -> 'BaseElement':
        element = type(self)()
        element._inner = self._inner
        return element

    def compile(self) -> str:
        return self._format.format(inner=self._inner)

    def __call__(self, inner: Union[None, str, 'BaseElement', MutableSequence['BaseElement']] = None) -> 'BaseElement':
        if inner:
            self._inner = self.set_inner(inner)
        return self.copy()

    def __repr__(self) -> str:
        return f'<{type(self).__name__} at {hex(id(self))}>'


class BaseTag(BaseElement):
    _name = _arguments = ''
    _is_closed = None
    _format = '<{name}{arguments}>{inner}'

    def __init__(self, name: str, is_closed: bool):
        if is_closed:
            self._format += '</{name}>'
        self._is_closed = is_closed
        self._name = name

    @staticmethod
    def set_arguments(*args, **kwargs):
        arguments = ''
        for key, value in kwargs.items():
            if key.endswith('_'):
                key = key[:-1]
            arguments += f' {key}={value}'

        for arg in args:
            if arg.endswith('_'):
                arg = arg[:-1]
            arguments += f' {arg}'

        return arguments

    def copy(self) -> 'BaseTag':
        tag = type(self)(self._name, self._is_closed)
        tag._inner = self._inner
        tag._arguments = self._arguments
        return tag

    def compile(self) -> str:
        return self._format.format(name=self._name, arguments=self._arguments, inner=self._inner)

    def __call__(self, inner: Union[None, str, 'BaseElement', MutableSequence['BaseElement']] = None, *args, **kwargs) -> 'Element':
        super().__call__(inner)
        if args or kwargs:
            self._arguments = self.set_arguments(*args, **kwargs)
        return self.copy()


class BaseHeadLocation:
    pass


class BaseBodyLocation:
    pass


class BaseUnallocatedLocation:
    pass


class UnallocatedTag(BaseTag, BaseUnallocatedLocation):
    pass


class HeadTag(BaseTag, BaseHeadLocation):
    pass


class BodyTag(BaseTag, BaseBodyLocation):
    pass


class BaseComponent(BaseElement):
    ELEMENTS = []

    def __call__(self, *args, **kwargs):
        if self.ELEMENTS:
            self._inner = self.set_inner(self.ELEMENTS)
        return self


class ComponentHead(BaseComponent, BaseHeadLocation):
    pass


class ComponentBody(BaseComponent, BaseBodyLocation):
    pass
