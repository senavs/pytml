from ...base.tags import BodyTag
from ...base.register import Register


@Register
class IFRAME(BodyTag):

    def __init__(self, **arguments):
        super().__init__('iframe', None, True, **arguments)
