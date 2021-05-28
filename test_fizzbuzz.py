from fizzbuzz import fizzbuzz
import unittest


class FizzbuzzTest(unittest.TestCase):
    # def test_fizzbuzz_push_0_should_be_return_0(self):
    #     result = fizzbuzz(0)
    #     self.assertEquals("0", result)

    def test_fizzbuzz_push_1_should_be_return_1(self):
        result = fizzbuzz(1)
        self.assertEquals("1", result)

    def test_fizzbuzz_push_2_should_be_return_bang(self):
        result = fizzbuzz(2)
        self.assertEquals("bang", result)

    def test_fizzbuzz_push_3_should_be_return_fizz(self):
        result = fizzbuzz(3)
        self.assertEquals("fizz", result)

    def test_fizzbuzz_push_4_should_be_return_bang(self):
        result = fizzbuzz(4)
        self.assertEquals("bang", result)

    def test_fizzbuzz_push_5_should_be_return_buzz(self):
        result = fizzbuzz(5)
        self.assertEquals("buzz", result)

    def test_fizzbuzz_push_6_should_be_return_fizz(self):
        result = fizzbuzz(6)
        self.assertEquals("fizz", result)

    def test_fizzbuzz_push_7_should_be_return_7(self):
        result = fizzbuzz(7)
        self.assertEquals("7", result)

    def test_fizzbuzz_push_8_should_be_return_bang(self):
        result = fizzbuzz(8)
        self.assertEquals("bang", result)

    def test_fizzbuzz_push_9_should_be_return_fizz(self):
        result = fizzbuzz(9)
        self.assertEquals("fizz", result)

    def test_fizzbuzz_push_10_should_be_return_buzz(self):
        result = fizzbuzz(10)
        self.assertEquals("buzz", result)

    def test_fizzbuzz_push_11_should_be_return_11(self):
        result = fizzbuzz(11)
        self.assertEquals("11", result)

    def test_fizzbuzz_push_12_should_be_return_fizz(self):
        result = fizzbuzz(12)
        self.assertEquals("fizz", result)

    def test_fizzbuzz_push_13_should_be_return_13(self):
        result = fizzbuzz(13)
        self.assertEquals("13", result)

    def test_fizzbuzz_push_14_should_be_return_bang(self):
        result = fizzbuzz(14)
        self.assertEquals("bang", result)

    def test_fizzbuzz_push_15_should_be_return_fizzbuzz(self):
        result = fizzbuzz(15)
        self.assertEquals("fizzbuzz", result)
