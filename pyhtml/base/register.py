class Register:
    """Register class"""
    __register_tags = {}

    def __new__(cls, other: object):
        """
        other (object): class that will be registered
        """
        cls.__register_tags[other.__name__.lower()] = other
        return other

    @classmethod
    def tags(cls) -> dict:
        """Get dict of all classes registered"""
        return cls.__register_tags.copy()
