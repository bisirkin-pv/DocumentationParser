from src.parser.IParser import IParser
import re


class Parser(IParser, ):
    """
    Разбор файлов на наличии документации
    """

    def __init__(self, reader):
        self.__reader = reader
        self.__doc_string = ''

    def parse(self):
        self.__reader.open()
        line = ''
        self.__doc_string = self._find_block()
        return line

    def _find_block(self):
        """
        Ищет блок с документацией
        :return:
        """
        text = ''
        start = False
        for x in self.__reader.get_line():
            match_begin = re.search(r'<[ ]*description', x.lower(), re.S)
            match_end = re.search(r'</[ ]*description[ ]*>', x.lower(), re.S)
            if match_begin is not None:
                start = True
            if match_end is not None:
                start = False
                text += x
            if start:
                text += x
        return text

    def find_tag_attribute(self, tag):
        pattern = '(?:{}[ ="]*)(\w*)(?:[ "]+)'.format(tag)
        match = re.search(pattern, self.__doc_string.lower(), re.S)
        if match is not None:
            x, y = match.regs[1]
            return self.__doc_string[x:y]
        return ''

    def find_tag(self, tag):
        pattern = '(?:<[ ]*{0}[ ]*>)(.*)(?:</[ ]*{0}[ ]*>)'.format(tag)
        match = re.search(pattern, self.__doc_string.lower(), re.S)
        if match is not None:
            x, y = match.regs[1]
            return self.__doc_string[x:y]
        return ''
