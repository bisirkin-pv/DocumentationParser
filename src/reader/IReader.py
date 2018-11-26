import abc


class IReader(abc.ABC):
    @abc.abstractmethod
    def open(self):
        """
        Возвращает текст файла
        :return: текст
        """
        pass
