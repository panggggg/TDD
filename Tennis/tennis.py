class Score:
    score = [0, 15, 30, 40, 45]

class Player:
    def __init__(self, name):
        self.name = name
        self.point = 0
    
    def get_score(self):
        return Score.score[self.point]

    def add_point(self):
        self.point += 1
        return self.point

class Scorer:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
    def get_score(self):
        if self.player1.get_score() == 45:
            return "Winner is A"
        if self.player2.get_score() == 45:
            return "Winner is B"
        if self.player1.get_score() == 40 and self.player2.get_score() == 40:
            return "Deuce"
        else:
            return f"{self.get_point(self.player1.get_score())} - {self.get_point(self.player2.get_score())}"
    
    def get_point(self, point):
        if point == 0:
            return "Lover"