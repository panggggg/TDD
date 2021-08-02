import unittest
from diamond import Diamond


class TestDiamond(unittest.TestCase):
    def test_number_of_left_right_push_A_line_1_should_be_return_0(self):
        expected = 0
        diamond = Diamond()
        actual = diamond.number_of_left_right(charector="A", line=1)
        self.assertEquals(expected, actual)

    def test_number_of_left_right_push_B_line_1_should_be_return_1(self):
        expected = 1
        diamond = Diamond()
        actual = diamond.number_of_left_right(charector="B", line=1)
        self.assertEquals(expected, actual)

    def test_number_of_left_right_push_C_line_1_should_be_return_2(self):
        expected = 2
        diamond = Diamond()
        actual = diamond.number_of_left_right(charector="C", line=1)
        self.assertEquals(expected, actual)

    def test_number_of_left_right_push_D_line_1_should_be_return_3(self):
        expected = 3
        diamond = Diamond()
        actual = diamond.number_of_left_right(charector="D", line=1)
        self.assertEquals(expected, actual)

    def test_number_of_left_right_push_B_line_2_should_be_return_0(self):
        expected = 0
        diamond = Diamond()
        actual = diamond.number_of_left_right(charector="B", line=2)
        self.assertEquals(expected, actual)

    def test_number_of_left_right_push_C_line_2_should_be_return_1(self):
        expected = 1
        diamond = Diamond()
        actual = diamond.number_of_left_right(charector="C", line=2)
        self.assertEquals(expected, actual)

    def test_number_of_left_right_push_D_line_2_should_be_return_2(self):
        expected = 2
        diamond = Diamond()
        actual = diamond.number_of_left_right(charector="D", line=2)
        self.assertEquals(expected, actual)