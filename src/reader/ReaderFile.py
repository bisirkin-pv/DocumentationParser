from src.reader.IReader import IReader


class ReaderFile(IReader):
    """
    Открывает указанный файл для дальнейшей работы с ним
    """
    def __init__(self, filename):
        """
        Конструктор
        :param filename: Имя файла
        """
        self.__filename = filename

    def open(self):
        with open(self.__filename, 'r', encoding='utf8') as file:
            lines = file.readlines()
        return lines
