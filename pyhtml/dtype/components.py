from pyhtml.dtype.base import ComponentHead, ComponentBody
from pyhtml.usable.tags import LINK_HEAD, SCRIPT_HEAD, OL, UL, LI


class Bootstrap4(ComponentHead):
    ELEMENTS = [LINK_HEAD(rel='stylesheet',
                          href='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css',
                          integrity='sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm',
                          crossorigin='anonymous'),
                SCRIPT_HEAD(src='https://code.jquery.com/jquery-3.2.1.slim.min.js',
                            integrity='sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN',
                            crossorigin='anonymous'),
                SCRIPT_HEAD(src='https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js',
                            integrity='sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q',
                            crossorigin='anonymous'),
                SCRIPT_HEAD(src='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js',
                            integrity='sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl',
                            crossorigin='anonymous')]


class OrderedList(ComponentBody):

    def __call__(self, *args, **kwargs):
        elements = []
        for arg in args:
            elements.append(LI(arg))
        self.ELEMENTS = OL(elements, **kwargs)
        return super().__call__()


class UnorderedList(ComponentBody):

    def __call__(self, *args, **kwargs):
        elements = []
        for arg in args:
            elements.append(LI(arg))
        self.ELEMENTS = UL(elements, **kwargs)
        return super().__call__()
