import unittest
import os
from src.reader.ReaderFile import ReaderFile


class TestReaderFile(unittest.TestCase):
    """
    Тест класса работы с файлом
    """
    TEST_FILE_BODY = 'hello world!\nThis is test'
    filename = 'test.txt'

    def setUp(self):
        with open(self.filename, 'w') as f:
            f.write(self.TEST_FILE_BODY)

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_open_file(self):
        reader = ReaderFile(self.filename)
        reader.open()
        line = ''
        for x in reader.get_line():
            line += x
        self.assertEqual(line, self.TEST_FILE_BODY)
