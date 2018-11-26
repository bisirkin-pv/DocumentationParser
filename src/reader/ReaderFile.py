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
        self.__lines = []

    def open(self):
        with open(self.__filename, 'r', encoding='utf8') as file:
            self.__lines = file.readlines()

    def get_line(self):
        count = 0
        while True:
            if count >= len(self.__lines):
                return
            count += 1
            yield self.__lines[count-1]

