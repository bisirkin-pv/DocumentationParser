import unittest
import os
from src.parser.Parser import Parser
from src.reader.ReaderFile import ReaderFile


class TestParse(unittest.TestCase):
    """
    Тест класса производящего разбор файла
    """
    TEST_FILE_BODY = '''
        hello world!
        <description status="work" tool="example">
            <name>Caption</name>
            <who>author</who>
            <params>
                <param name="param-name" type="string" title="text">
                <param name="param-name" type="string" title="text">
            </params>
<comment>
# Этот текст потом будет конвертирован в html
* параметр 1
* параметр 2
</comment>
        </description>
        another text
     '''
    filename = 'test.txt'

    def setUp(self):
        with open(self.filename, 'w') as f:
            f.write(self.TEST_FILE_BODY)
        reader = ReaderFile(self.filename)
        self.parser = Parser(reader)
        self.parser.parse()

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    # def test_parse(self):
    #     self.assertEqual(self.parser.parse(), self.TEST_FILE_BODY)

    def test_find_tag_attribute(self):
        self.assertEqual(self.parser.find_tag_attribute('status'), 'work')
        self.assertEqual(self.parser.find_tag_attribute('tool'), 'example')

    def test_find_tag(self):
        self.assertEqual(self.parser.find_tag('name'), 'Caption')
        self.assertEqual(self.parser.find_tag('who'), 'author')
        standard = """
# Этот текст потом будет конвертирован в html
* параметр 1
* параметр 2
"""
        self.assertEqual(self.parser.find_tag('comment'), standard)

