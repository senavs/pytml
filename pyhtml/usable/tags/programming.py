from typing import Union

from ...base.tags import BodyTag
from ...base.register import Register


@Register
class SCRIPT(BodyTag):

    def __init__(self, inner: Union[None, str], **arguments):
        super().__init__('script', inner, False, **arguments)
