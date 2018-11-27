from collections import namedtuple

CommentTuple = namedtuple('Comment', 'name status who tool text')


class Comment:
    """
    Объект разобранной строки описания
    """

    def __init__(self, comment_tuple):
        self.name, self.status, self.who, self.tool, self.text = comment_tuple
        self.__params = []

    def set_param(self, comment_param):
        """
        Устанавливает параметры
        :param comment_param: Кортеж параметров
        :return:
        """
        self.__params.append(comment_param)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.name!r},{self.status!r},{self.tool!r})'
                )

    def __str__(self):
        return f'Коммент: {self.name}'
