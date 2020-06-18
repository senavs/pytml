from typing import Union, MutableSequence


class BaseElement:
    """Classe Base para qualquer elemento HTML"""

    _inner = ''
    _format = '{inner}'

    @staticmethod
    def set_inner(value: Union[None, 'BaseElement', MutableSequence['BaseElement']] = None) -> str:
        """Setar valor do elemento

        :param value: valor do elemento
            :type: Union[None, 'BaseElement', MutableSequence['BaseElement']]

        :return: str
        """

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
        """Copiar elemento e seu valores

        :return: 'BaseElement'
        """

        element = type(self)()
        element._inner = self._inner
        return element

    def compile(self) -> str:
        """Renderizar elemento como string"""

        return self._format.format(inner=self._inner)

    def __call__(self, inner: Union[None, str, 'BaseElement', MutableSequence['BaseElement']] = None) -> 'BaseElement':
        """Criar uma cópia e setar valor

        :param inner: valor do elemento
            :type: Union[None, str, 'BaseElement', MutableSequence['BaseElement']]

        :return: 'BaseElement'
        """

        if inner:
            self._inner = self.set_inner(inner)
        return self.copy()

    def __repr__(self) -> str:
        return f'<{type(self).__name__} at {hex(id(self))}>'


class BaseTag(BaseElement):
    """Classe Base para qualquer elemento HTML"""

    _name = _arguments = ''
    _is_closed = None
    _format = '<{name}{arguments}>{inner}'

    def __init__(self, name: str, is_closed: bool):
        """ Construtor

        :param name: tome da tag
            :type: str
        :param is_closed: chave fecha </x>
            :type: bool
        """

        if is_closed:
            self._format += '</{name}>'
        self._is_closed = is_closed
        self._name = name

    @staticmethod
    def set_arguments(*args, **kwargs) -> str:
        """Setar valor do argumentos da tag

        :return: str
        """

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
        """Copiar tag e seu valores

        :return: 'BaseTag'
        """

        tag = type(self)(self._name, self._is_closed)
        tag._inner = self._inner
        tag._arguments = self._arguments
        return tag

    def compile(self) -> str:
        """Renderizar tag como string"""

        return self._format.format(name=self._name, arguments=self._arguments, inner=self._inner)

    def __call__(self, inner: Union[None, str, 'BaseElement', MutableSequence['BaseElement']] = None, *args, **kwargs) -> 'BaseTag':
        """Criar uma cópia e setar valor

        :param inner: valor do elemento
            :type: Union[None, str, 'BaseElement', MutableSequence['BaseElement']]

        :return: 'BaseTag'
        """

        super().__call__(inner)
        if args or kwargs:
            self._arguments = self.set_arguments(*args, **kwargs)
        return self.copy()


class BaseHeadLocation:
    """Classe base para setar a localização do elemento no HEAD"""


class BaseBodyLocation:
    """Classe base para setar a localização do elemento no BODY"""


class BaseUnallocatedLocation:
    """Classe base para setar a localização do elemento no HTML"""


class UnallocatedTag(BaseTag, BaseUnallocatedLocation):
    """Classe tag loxalizada no HTML"""


class HeadTag(BaseTag, BaseHeadLocation):
    """Classe tag loxalizada no HEAD"""


class BodyTag(BaseTag, BaseBodyLocation):
    """Classe tag loxalizada no BODY"""


class BaseComponent(BaseElement):
    """Casse base de compnentes HTML"""

    ELEMENTS = []

    def __call__(self, *args, **kwargs):
        if self.ELEMENTS:
            self._inner = self.set_inner(self.ELEMENTS)
        return self


class ComponentHead(BaseComponent, BaseHeadLocation):
    """Classe tag loxalizada no HEAD"""


class ComponentBody(BaseComponent, BaseBodyLocation):
    """Classe tag loxalizada no BODY"""
