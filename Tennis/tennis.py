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

