from typing import Union, Tuple, Dict

from ..dtypes.base import Component
from ..tags.link import LINK
from ..tags.programming import SCRIPT_HEAD


class Bootstrap4(Component):

    def __call__(self, **kwargs):
        self.inner = [LINK(rel="stylesheet",
                           href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css",
                           integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh",
                           crossorigin="anonymous"),
                      SCRIPT_HEAD(src="https://code.jquery.com/jquery-3.4.1.slim.min.js",
                                  integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n",
                                  crossorigin="anonymous"),
                      SCRIPT_HEAD(src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js",
                                  integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo",
                                  crossorigin="anonymous"),
                      SCRIPT_HEAD(src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js",
                                  integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6",
                                  crossorigin="anonymous")]
        self._loaded = True
        return self.compile()

