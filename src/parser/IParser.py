import abc


class IParser(abc.ABC):
    @abc.abstractmethod
    def parse(self):
        """
        Разбирает текст на наличии документации и возвращает её
        :return: Comment
        """
        pass
