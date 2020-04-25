from ..base.tags import Tag
from ..usable.tags.basic import DOCTYPE, HTML, HEAD, BODY


class DOM:
    __dom_head = []
    __dom_body = []

    def __init__(self, file_path: str):
        self.file = open(file_path, 'w')
        self.file_path = file_path

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        web_page = DOCTYPE(HTML([HEAD(self.__dom_head), BODY(self.__dom_body)]))

        self.file.write(web_page.render())
        self.file.close()

    def _register_in_head(self, tag: Tag):
        self.__dom_head.append(tag)

    def _register_in_body(self, tag: Tag):
        self.__dom_body.append(tag)
