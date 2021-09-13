import unittest
from roman import integer_to_roman

class TestIntegerToRoman(unittest.TestCase):
    def test_input_num_1_return_I(self):
        expected = "I"
        actual = integer_to_roman(num=1)
        self.assertEquals(expected, actual)

    def test_input_num_2_return_II(self):
        expected = "II"
        actual = integer_to_roman(num=2)
        self.assertEquals(expected, actual)

    def test_input_num_3_return_III(self):
        expected = "III"
        actual = integer_to_roman(num=3)
        self.assertEquals(expected, actual)

    def test_input_num_4_return_IV(self):
        expected = "IV"
        actual = integer_to_roman(num=4)
        self.assertEquals(expected, actual)

    def test_input_num_5_return_V(self):
        expected = "V"
        actual = integer_to_roman(num=5)
        self.assertEquals(expected, actual)

    def test_input_num_6_return_VI(self):
        expected = "VI"
        actual = integer_to_roman(num=6)
        self.assertEquals(expected, actual)

    def test_input_num_7_return_VII(self):
        expected = "VII"
        actual = integer_to_roman(num=7)
        self.assertEquals(expected, actual)

    def test_input_num_8_return_VIII(self):
        expected = "VIII"
        actual = integer_to_roman(num=8)
        self.assertEquals(expected, actual)

    def test_input_num_9_return_IX(self):
        expected = "IX"
        actual = integer_to_roman(num=9)
        self.assertEquals(expected, actual)

    def test_input_num_10_return_X(self):
        expected = "X"
        actual = integer_to_roman(num=10)
        self.assertEquals(expected, actual)
    
    def test_input_num_11_return_XI(self):
        expected = "XI"
        actual = integer_to_roman(num=11)
        self.assertEquals(expected, actual)

    def test_input_num_29_return_XXIX(self):
        expected = "XXIX"
        actual = integer_to_roman(num=29)
        self.assertEquals(expected, actual)

    def test_input_num_38_return_XXXVIII(self):
        expected = "XXXVIII"
        actual = integer_to_roman(num=38)
        self.assertEquals(expected, actual)

    def test_input_num_1998_return_MCMXCVIII(self):
        expected = "MCMXCVIII"
        actual = integer_to_roman(num=1998)
        self.assertEquals(expected, actual)