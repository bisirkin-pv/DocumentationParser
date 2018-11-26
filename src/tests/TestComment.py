import unittest
from src.comment.Comment import Comment, CommentTuple


class TestComment(unittest.TestCase):
    """
    Тестирование объекта комментария
    """

    def test_create_comment(self):
        name = 'text comment'
        status = 'work'
        tool = 'tools'
        text = 'example'
        standard = "Comment('{}','{}','{}')".format(name, status, tool)
        comment_tuple = CommentTuple(name, status, tool, text)
        comment = Comment(comment_tuple)
        self.assertEqual(standard, repr(comment))
