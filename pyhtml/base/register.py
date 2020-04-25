class Register:
    __register_tags = {}

    def __new__(cls, other: object):
        cls.__register_tags[other.__name__.lower()] = other
        return other

    @classmethod
    def tags(cls) -> dict:
        return cls.__register_tags.copy()
