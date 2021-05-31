from roman_numeral import int_to_roman
import unittest
from unittest import result


class roman_test(unittest.TestCase):
    def input_55_should_be_return_LV(self):
        result = int_to_roman(55)
        self.assertEquals("LV", result)