from pyhtml.dtype.base import BaseElement, BaseHeadLocation, BaseBodyLocation
from pyhtml.usable.tags import HTML, HEAD, BODY


class Page:
    """Classe DOM"""

    def __init__(self, file_path: str):
        """Contrutor

        :param file_path: diretório onde será salvo o arquivo HTML
            :type: str
        """

        self.file_path = file_path
        self.file = None
        self._head_elements = []
        self._body_elements = []

    def __enter__(self):
        self.file = open(self.file_path, 'w')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        head = HEAD(self._head_elements)
        body = BODY(self._body_elements)
        page = HTML([head, body])

        self.file.write(page.compile())
        self.file.close()

    def register(self, element: BaseElement):
        """Registar tag ou componente da página HTML

        :param element: tag ou elemento a ser registrado
            :type: 'BaseElement'
        """

        if isinstance(element, BaseHeadLocation):
            self._head_elements.append(element)
        elif isinstance(element, BaseBodyLocation):
            self._body_elements.append(element)
        else:
            raise ValueError('try BaseHeadLocation and BaseBodyLocation subclasses')
