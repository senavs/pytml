from ..essential.tag import Tag
from ..tags.basic import HTML, HEAD, BODY


class Page:

    def __init__(self, file_path: str, mode: str = 'w'):
        self._file_path = str(file_path)
        self._mode = str(mode)

        self._file = None

        self._register_tags = {'head': [], 'body': []}

    def register(self, location: str, element: Tag):
        if location.lower() not in ('head', 'body'):
            raise ValueError('can only register elements in head or body in HTML')

        self._register_tags[location].append(element)

    def open(self) -> 'Page':
        self._file = open(self._file_path, self._mode)
        return self

    def close(self):
        head = HEAD(self._register_tags['head'])
        body = BODY(self._register_tags['body'])
        page = HTML([head, body])

        self._file.write(page.render())
        self._file.close()

    def __enter__(self) -> 'Page':
        return self.open()

    def __exit__(self, exc_type, exc_val, exc_tb):
        head = HEAD(self._register_tags['head'])
        body = BODY(self._register_tags['body'])
        page = HTML([head, body])

        self._file.write(page.render())
        self._file.close()
