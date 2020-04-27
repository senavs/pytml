from typing import Union, List


class Tag:
    """Base tag class"""

    __tag_format = '<{name}{arguments}>{inner}'
    __name = __arguments = __inner = ''

    def __init__(self, name: str, inner: Union[None, str, 'Tag', List['Tag']], is_closed: bool, **arguments):
        """
        Parameters
        name (str): html tag name. it will appeared in <> element
        inner (None) or (str) or (Tag) or (List[Tag]): what goes inside the tag <tag> whats_going_where </tag>
        is_closed (bool): if the tag is needed to be closed. like </tag>
        **arguments: tag arguments. like class, id and style. if the argument is a python keywords, use _ at the end.
        """
        self.name = name
        self.arguments = arguments
        self.inner = inner

        if is_closed:
            self.__tag_format += f'</{self.name}>'

    @property
    def name(self) -> str:
        """Tag name getter"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Tag name setter"""
        self.__name = value

    @property
    def arguments(self) -> str:
        """Tag arguments getter"""
        return self.__arguments

    @arguments.setter
    def arguments(self, arguments: dict):
        """Tag arguments setter"""
        if arguments:
            for key, value in arguments.items():
                if str(key).endswith('_'):
                    key = key[:-1]
                self.__arguments += f' {key}="{value}"'

    @property
    def inner(self) -> str:
        """Tag inner elements getter"""
        return self.__inner

    @inner.setter
    def inner(self, elements: Union[str, 'Tag', List['Tag']]):
        """Tag inner elements setter"""
        if elements:
            if isinstance(elements, Tag):
                self.__inner = elements.render()
            elif isinstance(elements, List):
                self.__inner = ''.join(element.render() for element in elements)
            else:
                self.__inner = elements

    def render(self) -> str:
        """
        Get tag params and render it into <tag> element

        Return
        render tag (str): html tag. like <div class='some-class' id='div-1'><h1>hello world!</h1></div>
        """
        return self.__tag_format.format(name=self.name, arguments=self.arguments, inner=self.inner)

    def __repr__(self):
        return self.render()


class HeadTag(Tag):
    """Class to identify head tags"""


class BodyTag(Tag):
    """Class to identify body tags"""


class UnrecordableTag(Tag):
    """Class to identify unrecordable tags"""
