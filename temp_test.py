import unittest
from temp_converter import*

class testTempConverter(unittest.TestCase):
    def getTempConversion(self):
        result=convertTemp("80")
        self.assertEqual(result, 26.6)


    def test_Input(self):
        with unittest.mock.patch('builtins.input',return_value="90"):
            self.assertEqual(test_Input(),"91")