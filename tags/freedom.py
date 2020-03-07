from essential.tag import Tag


class META(Tag):

    def __init__(self, charset: str, **kwargs):
        kwargs.update(charset=charset)
        super().__init__('meta', '', False, **kwargs)


class BR(Tag):

    def __init__(self, **kwargs):
        super().__init__('br', '', False, **kwargs)


class HR(Tag):

    def __init__(self, **kwargs):
        super().__init__('hr', '', False, **kwargs)
