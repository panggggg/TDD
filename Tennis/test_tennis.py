import unittest
from tennis import Player, Scorer

class TestTennis(unittest.TestCase):
    # def test_player_get_score_0_0(self):
    #     expected = "0 - 0"
    #     a = Player("A")
    #     b = Player("B")
    #     self.assertEquals(expected, f"{a.get_score()} - {b.get_score()}")

    # def test_add_point_player_get_score_15_0(self):
    #     expected = "15 - 0"
    #     a = Player("A")
    #     b = Player("B")
    #     a.add_point()
    #     self.assertEquals(expected, f"{a.get_score()} - {b.get_score()}")

    # def test_add_point_player_get_score_15_15(self):
    #     expected = "15 - 15"
    #     a = Player("A")
    #     b = Player("B")
    #     a.add_point()
    #     b.add_point()
    #     self.assertEquals(expected, f"{a.get_score()} - {b.get_score()}")

    # def test_add_point_player_get_score_30_15(self):
    #     expected = "30 - 15"
    #     a = Player("A")
    #     b = Player("B")
    #     a.add_point()
    #     a.add_point()
    #     b.add_point()
    #     self.assertEquals(expected, f"{a.get_score()} - {b.get_score()}")

    def test_scorer_player_A_get_point_0_0(self):
        expected = "Lover - Lover"
        a = Player("A")
        b = Player("B")
        score = Scorer(a, b)
        self.assertEquals(expected, score.get_score())

    def test_scorer_player_A_get_point_15_0(self):
        expected = "Fifthteen - Lover"
        a = Player("A")
        b = Player("B")
        a.add_point()
        score = Scorer(a, b)
        self.assertEquals(expected, score.get_score())

    def test_scorer_player_A_get_point_30_0(self):
        expected = "Thirty - Lover"
        a = Player("A")
        b = Player("B")
        a.add_point()
        a.add_point()
        score = Scorer(a, b)
        self.assertEquals(expected, score.get_score())

    def test_scorer_player_A_get_point_40_0(self):
        expected = "Fourty - Lover"
        a = Player("A")
        b = Player("B")
        a.add_point()
        a.add_point()
        a.add_point()
        score = Scorer(a, b)
        self.assertEquals(expected, score.get_score())

    def test_scorer_player_A_get_point_45_0(self):
        expected = "Winner is A"
        a = Player("A")
        b = Player("B")
        a.add_point()
        a.add_point()
        a.add_point()
        a.add_point()
        score = Scorer(a, b)
        self.assertEquals(expected, score.get_score())

    def test_scorer_player_B_get_point_0_0(self):
        expected = "Lover - Lover"
        a = Player("A")
        b = Player("B")
        score = Scorer(a, b)
        self.assertEquals(expected, score.get_score())

    def test_scorer_player_B_get_point_15_0(self):
        expected = "Lover - Fifthteen"
        a = Player("A")
        b = Player("B")
        b.add_point()
        score = Scorer(a, b)
        self.assertEquals(expected, score.get_score())

    def test_scorer_player_B_get_point_30_0(self):
        expected = "Lover - Thirty"
        a = Player("A")
        b = Player("B")
        b.add_point()
        b.add_point()
        score = Scorer(a, b)
        self.assertEquals(expected, score.get_score())

    def test_scorer_player_A_get_point_40_0(self):
        expected = "Lover - Fourty"
        a = Player("A")
        b = Player("B")
        b.add_point()
        b.add_point()
        b.add_point()
        score = Scorer(a, b)
        self.assertEquals(expected, score.get_score())

    def test_scorer_player_B_get_point_45_0(self):
        expected = "Winner is B"
        a = Player("A")
        b = Player("B")
        b.add_point()
        b.add_point()
        b.add_point()
        b.add_point()
        score = Scorer(a, b)
        self.assertEquals(expected, score.get_score())

    def test_scorer_get_point_30_15(self):
        expected = "Thirty - Fifthteen"
        a = Player("A")
        b = Player("B")
        a.add_point()
        a.add_point()
        b.add_point()
        score = Scorer(a, b)
        self.assertEquals(expected, score.get_score())

    def test_scorer_deuce(self):
        expected = "Deuce"
        a = Player("A")
        b = Player("B")
        a.add_point()
        a.add_point()
        a.add_point()
        b.add_point()
        b.add_point()
        b.add_point()
        score = Scorer(a, b)
        self.assertEquals(expected, score.get_score())

    def test_player_A_get_Advantage(self):
        expected = "Advantage A"
        a = Player("A")
        b = Player("B")
        a.add_point()
        a.add_point()
        a.add_point()
        a.add_point()
        b.add_point()
        b.add_point()
        b.add_point()
        score = Scorer(a, b)
        self.assertEquals(expected, score.get_score())

    def test_player_A_Advantage_get_point(self):
        expected = "Winner is A"
        a = Player("A")
        b = Player("B")
        a.add_point()
        a.add_point()
        a.add_point()
        a.add_point()
        a.add_point()
        b.add_point()
        b.add_point()
        b.add_point()
        score = Scorer(a, b)
        self.assertEquals(expected, score.get_score())

    def test_player_B_get_Advantage(self):
        expected = "Advantage B"
        a = Player("A")
        b = Player("B")
        a.add_point()
        a.add_point()
        a.add_point()
        b.add_point()
        b.add_point()
        b.add_point()
        b.add_point()
        score = Scorer(a, b)
        self.assertEquals(expected, score.get_score())

    def test_player_B_get_Advantage_get_point(self):
        expected = "Winner is B"
        a = Player("A")
        b = Player("B")
        a.add_point()
        a.add_point()
        a.add_point()
        b.add_point()
        b.add_point()
        b.add_point()
        b.add_point()
        b.add_point()
        score = Scorer(a, b)
        self.assertEquals(expected, score.get_score())

    # def test_scorer_player_B_is_winner(self):
    #     expected = "Winner is B"
    #     a = Player("A")
    #     b = Player("B")
    #     b.add_point()
    #     b.add_point()
    #     b.add_point()
    #     b.add_point()
    #     score = Scorer(a, b)
    #     self.assertEquals(expected, score.get_score())

    # def test_scorer_is_deuce(self):
    #     expected = "Deuce"
    #     a = Player("A")
    #     b = Player("B")
    #     b.add_point()
    #     b.add_point()
    #     b.add_point()
    #     a.add_point()
    #     a.add_point()
    #     a.add_point()
    #     score = Scorer(a, b)
    #     self.assertEquals(expected, score.get_score())

    # def test_get_point_0_0_should_be_return_lover_lover(self):
    #     expected = "Lover - Lover"
    #     a = Player("A")
    #     b = Player("B")
    #     score = Scorer(a, b)
    #     self.assertEquals(expected, score.get_score())

    # def test_get_point_15_0_should_be_return_fifthteen_lover(self):
    #     expected = "Fifthteen - Lover"
    #     a = Player("A")
    #     b = Player("B")
    #     a.add_point()
    #     score = Scorer(a, b)
    #     self.assertEquals(expected, score.get_score())

    
    