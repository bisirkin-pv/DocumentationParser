from typing import NamedTuple


class CommentParam(NamedTuple):
    """
    Кортеж описания параметров
    """
    name: str
    type: str
    text: str
