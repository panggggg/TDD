import unittest
from print_square import Square


class test_print_square(unittest.TestCase):
    def setUp(self):
        self.square = Square()

    def test_input_number_1_line_1(self):
        expexted = "#"
        actual = self.square.print_square(number=1, line=1)
        self.assertEquals(expexted, actual)