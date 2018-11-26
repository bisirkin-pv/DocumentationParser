import abc


class IReader(abc.ABC):
    @abc.abstractmethod
    def open(self):
        """
        Возвращает текст файла
        :return: текст
        """
        pass

    @abc.abstractmethod
    def get_line(self):
        """
        Возвращает файл по строчно
        :return: генератор
        """
        pass
