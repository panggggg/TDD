from fizzbuzz import fizzbuzz
import unittest


class FizzbuzzTest(unittest.TestCase):
    def test_fizzbuzz_push_1_should_be_return_1(self):
        result = fizzbuzz(1)
        self.assertEquals("1", result)

    # def test_fizzbuzz_push_2_should_be_return_bang(self):
    #     result = fizzbuzz(2)
    #     self.assertEquals("bang", result)

    # def test_fizzbuzz_push_3_should_be_return_fizz(self):
    #     result = fizzbuzz(3)
    #     self.assertEquals("fizz", result)

    # def test_fizzbuzz_push_15_should_be_return_fizzbuzz(self):
    #     result = fizzbuzz(15)
    #     self.assertEquals("fizzbuzz", result)
