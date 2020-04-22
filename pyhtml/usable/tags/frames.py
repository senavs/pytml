from pyhtml.base.tags import BodyTag


class IFRAME(BodyTag):

    def __init__(self, **arguments):
        super().__init__('iframe', None, True, **arguments)
