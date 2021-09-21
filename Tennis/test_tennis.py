import unittest
from tennis import Player

class TestTennis(unittest.TestCase):
    def test_player_get_score_0_0(self):
        expected = "0 - 0"
        a = Player("A")
        b = Player("B")
        score_a = a.get_score("0")
        score_b = b.get_score("0")
        self.assertEquals(expected, f"{score_a} - {score_b}")