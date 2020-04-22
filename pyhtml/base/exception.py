class TagError(Exception):
    """Tag error base exception class"""


class TagNotFoundError(TagError):
    """Tag was not found"""


class TagNotRecordable(TagError):
    """Tag is not allow to register"""
