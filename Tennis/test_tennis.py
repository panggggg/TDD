import unittest
from tennis import Player

class TestTennis(unittest.TestCase):
    def test_player_get_score_0_0(self):
        expected = "0 - 0"
        a = Player("A")
        b = Player("B")
        a_score = a.get_score("0")
        b_score = b.get_score("0")
        self.assertEquals(expected, f"{a_score} - {b_score}")

    def test_player_get_score_15_0(self):
        expected = "15 - 0"
        a = Player("A")
        b = Player("B")
        a_score = a.get_score("15")
        b_score = b.get_score("0")
        self.assertEquals(expected, f"{a_score} - {b_score}")