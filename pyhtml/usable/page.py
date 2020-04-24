from ..base.dom import DOM
from ..base.tags import Tag, HeadTag, BodyTag
from ..base.exception import TagNotRecordable


class Page(DOM):

    def __init__(self, file_path: str):
        super().__init__(file_path)

    def register(self, tag: Tag):
        if isinstance(tag, HeadTag):
            self._register_in_head(tag)
        elif isinstance(tag, BodyTag):
            self._register_in_body(tag)
        else:
            raise TagNotRecordable(f'{tag} is not recordable. try any HeadTag or BodyTag.')
