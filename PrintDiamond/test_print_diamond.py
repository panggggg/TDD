import unittest
from print_diamond import Diamond


class TestPrintDiamond(unittest.TestCase):
    def setUp(self):
        self.diamond = Diamond()

    def test_right_space_push_charecter_A_should_be_return_list_0_space(self):
        right_space = ""
        expected = right_space
        actual = self.diamond.print_right_space("A")
        self.assertEquals(expected, actual)

    def test_right_space_push_charecter_B_should_be_return_list_0_1(self):
        right_space = "\n."
        expected = right_space
        actual = self.diamond.print_right_space("B")
        self.assertEquals(expected, actual)

    def test_right_space_push_charecter_C_should_be_return_list_0_1_2(self):
        right_space = "\n.\n.."
        expected = right_space
        actual = self.diamond.print_right_space("C")
        self.assertEquals(expected, actual)

    def test_right_space_push_charecter_D_should_be_return_list_0_1_2_3(self):
        right_space = "\n.\n..\n..."
        expected = right_space
        actual = self.diamond.print_right_space("D")
        self.assertEquals(expected, actual)

    ############################################################################################

    def test_middle_space_push_charecter_A_should_be_return_list_0(self):
        list_left_space = [0]
        expected = list_left_space
        actual = self.diamond.print_middle_space("A")
        self.assertEquals(expected, actual)

    def test_middle_space_push_charecter_B_should_be_return_list_0_1(self):
        list_left_space = [0, 1]
        expected = list_left_space
        actual = self.diamond.print_middle_space("B")
        self.assertEquals(expected, actual)

    def test_middle_space_push_charecter_C_should_be_return_list_0_1_3(self):
        list_left_space = [0, 1, 3]
        expected = list_left_space
        actual = self.diamond.print_middle_space("C")
        self.assertEquals(expected, actual)

    def test_middle_space_push_charecter_D_should_be_return_list_0_1_3_5(self):
        list_left_space = [0, 1, 3, 5]
        expected = list_left_space
        actual = self.diamond.print_middle_space("D")
        self.assertEquals(expected, actual)