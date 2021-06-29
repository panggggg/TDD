import unittest
from print_diamond import Diamond


class TestPrintDiamond(unittest.TestCase):
    def setUp(self):
        self.diamond = Diamond()

    def test_count_space_push_A_left_line_1(self):
        expected = 0
        actual = self.diamond.count_space(charecter="A", type="left", line=1)
        self.assertEquals(expected, actual)

    def test_count_space_push_B_left_line_1(self):
        expected = 1
        actual = self.diamond.count_space(charecter="B", type="left", line=1)
        self.assertEquals(expected, actual)

    def test_count_space_push_C_left_line_1(self):
        expected = 2
        actual = self.diamond.count_space(charecter="C", type="left", line=1)
        self.assertEquals(expected, actual)

    def test_count_space_push_C_left_line_4(self):
        expected = 1
        actual = self.diamond.count_space(charecter="C", type="left", line=4)
        self.assertEquals(expected, actual)

    def test_count_space_push_C_left_line_5(self):
        expected = 2
        actual = self.diamond.count_space(charecter="C", type="left", line=5)
        self.assertEquals(expected, actual)

    def test_count_space_push_E_left_line_6(self):
        expected = 1
        actual = self.diamond.count_space(charecter="E", type="left", line=6)
        self.assertEquals(expected, actual)

    def test_count_space_push_E_left_line_7(self):
        expected = 2
        actual = self.diamond.count_space(charecter="E", type="left", line=7)
        self.assertEquals(expected, actual)

    def test_count_space_push_C_middle_line_1(self):
        expected = 0
        actual = self.diamond.count_space(charecter="C", type="middle", line=1)
        self.assertEquals(expected, actual)

    def test_count_space_push_C_middle_line_2(self):
        expected = 1
        actual = self.diamond.count_space(charecter="C", type="middle", line=2)
        self.assertEquals(expected, actual)

    def test_count_space_push_C_middle_line_3(self):
        expected = 3
        actual = self.diamond.count_space(charecter="C", type="middle", line=3)
        self.assertEquals(expected, actual)

    def test_count_space_push_C_middle_line_4(self):
        expected = 1
        actual = self.diamond.count_space(charecter="C", type="middle", line=4)
        self.assertEquals(expected, actual)

    def test_count_space_push_D_middle_line_4(self):
        expected = 5
        actual = self.diamond.count_space(charecter="D", type="middle", line=4)
        self.assertEquals(expected, actual)

    def test_count_space_push_D_middle_line_5(self):
        expected = 3
        actual = self.diamond.count_space(charecter="D", type="middle", line=5)
        self.assertEquals(expected, actual)

    def test_count_space_push_D_middle_line_6(self):
        expected = 1
        actual = self.diamond.count_space(charecter="D", type="middle", line=6)
        self.assertEquals(expected, actual)

    def test_count_space_push_E_middle_line_6(self):
        expected = 5
        actual = self.diamond.count_space(charecter="E", type="middle", line=6)
        self.assertEquals(expected, actual)

    def test_count_space_push_E_middle_line_7(self):
        expected = 3
        actual = self.diamond.count_space(charecter="E", type="middle", line=7)
        self.assertEquals(expected, actual)

    def test_count_space_push_E_middle_line_8(self):
        expected = 1
        actual = self.diamond.count_space(charecter="E", type="middle", line=8)
        self.assertEquals(expected, actual)

    ##########################################################################################

    def test_print_diamond_push_A_line_1(self):
        expected = "A"
        actual = self.diamond.print_diamond(charecter="A", line=1)
        self.assertEquals(expected, actual)

    def test_print_diamond_push_B_line_1(self):
        expected = ".A."
        actual = self.diamond.print_diamond(charecter="B", line=1)
        self.assertEquals(expected, actual)

    def test_print_diamond_push_B_line_2(self):
        expected = "B.B"
        actual = self.diamond.print_diamond(charecter="B", line=2)
        self.assertEquals(expected, actual)

    def test_print_diamond_push_B_line_3(self):
        expected = ".A."
        actual = self.diamond.print_diamond(charecter="B", line=3)
        self.assertEquals(expected, actual)

    def test_print_diamond_push_C_line_1(self):
        expected = "..A.."
        actual = self.diamond.print_diamond(charecter="C", line=1)
        self.assertEquals(expected, actual)

    def test_print_diamond_push_D_line_1(self):
        expected = "...A..."
        actual = self.diamond.print_diamond(charecter="D", line=1)
        self.assertEquals(expected, actual)