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

    # def test_left_space_push_charecter_B_should_be_return_list_0_1(self):
    #     left_space = ".\n"
    #     expected = left_space
    #     actual = self.diamond.print_left_space("B")
    #     self.assertEquals(expected, actual)

    # def test_left_space_push_charecter_C_should_be_return_list_0_1_2(self):
    #     left_space = "..\n.\n"
    #     expected = left_space
    #     actual = self.diamond.print_left_space("C")
    #     self.assertEquals(expected, actual)

    # def test_left_space_push_charecter_D_should_be_return_list_0_1_2_3(self):
    #     left_space = "...\n..\n.\n"
    #     expected = left_space
    #     actual = self.diamond.print_left_space("D")
    #     self.assertEquals(expected, actual)

    ############################################################################################

    # def test_right_space_push_charecter_A_should_be_return_list_0_space(self):
    #     right_space = ""
    #     expected = right_space
    #     actual = self.diamond.print_right_space("A")
    #     self.assertEquals(expected, actual)

    # def test_right_space_push_charecter_B_should_be_return_list_0_1(self):
    #     right_space = ".\n"
    #     expected = right_space
    #     actual = self.diamond.print_right_space("B")
    #     self.assertEquals(expected, actual)

    # def test_right_space_push_charecter_C_should_be_return_list_0_1_2(self):
    #     right_space = "..\n .\n"
    #     expected = right_space
    #     actual = self.diamond.print_right_space("C")
    #     self.assertEquals(expected, actual)

    # def test_right_space_push_charecter_D_should_be_return_list_0_1_2_3(self):
    #     right_space = "...\n ..\n .\n"
    #     expected = right_space
    #     actual = self.diamond.print_right_space("D")
    #     self.assertEquals(expected, actual)

    # ############################################################################################

    # def test_middle_space_push_charecter_A_should_be_return_list_0(self):
    #     middle_space = ""
    #     expected = middle_space
    #     actual = self.diamond.print_middle_space("A")
    #     self.assertEquals(expected, actual)

    # def test_middle_space_push_charecter_B_should_be_return_list_0_1(self):
    #     middle_space = "[0, 1]"
    #     expected = middle_space
    #     actual = self.diamond.print_middle_space("B")
    #     self.assertEquals(expected, actual)

    # def test_middle_space_push_charecter_C_should_be_return_list_0_1_3(self):
    #     middle_space = [0, 1, 3]
    #     expected = middle_space
    #     actual = self.diamond.print_middle_space("C")
    #     self.assertEquals(expected, actual)

    # def test_middle_space_push_charecter_D_should_be_return_list_0_1_3_5(self):
    #     middle_space = [0, 1, 3, 5]
    #     # ("  .  \n ...\n.....\n ...\n  .  ")
    #     expected = middle_space
    #     actual = self.diamond.print_middle_space("D")
    #     self.assertEquals(expected, actual)