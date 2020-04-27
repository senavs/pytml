from typing import Union, Tuple, List

from pyhtml.base.tags import BodyTag, Tag


class Component(BodyTag):
    """Base component class"""

    def __init__(self, root_tag: str, inner: Union[Tag, List[Tag]], **arguments):
        """
        Parameters
        inner (None) or (str) or (Tag) or (List[Tag]): what goes inside the tag <tag> whats_going_where </tag>
        **arguments: tag arguments. like class, id and style. if the argument is a python keywords, use _ at the end.
        """
        super().__init__(root_tag, inner, True, **arguments)
