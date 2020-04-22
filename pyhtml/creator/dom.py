from typing import Union
from abc import abstractmethod

from pyhtml.concrete.basic import DOCTYPE, HTML, HEAD, BODY


class DOM:
    __dom_head = []
    __dom_body = []

    def __init__(self, file_path: str):
        self.file = open(file_path, 'w')
        self.file_path = file_path

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        web_page = DOCTYPE(HTML([HEAD(self.__dom_head), BODY(None, self.__dom_body)]))

        self.file.write(web_page.render())
        self.file.close()

    @abstractmethod
    def register_in_head(self, tag: str, arguments: Union[None, dict]):
        """Register Tags into __dom_head"""

    @abstractmethod
    def register_in_body(self, tag: str, arguments: Union[None, dict]):
        """Register Tags into __dom_body"""
