class Player:
    def __init__(self, name):
        self.name = name
        self.point = 0
    
    def get_point(self):
        return self.point

    def add_point(self):
        self.point += 1
        return self.point
    
    def get_name(self):
        return self.name

class Scorer:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
    def get_score(self):
        player1_point = self.player1.get_point()
        player2_point = self.player2.get_point()
        if  player1_point == 4 and player2_point < 3:
            return f"Winner is {self.player1.get_name()}"
        if player2_point == 4 and  player1_point < 3:
            return f"Winner is {self.player2.get_name()}"
        if  player1_point >= 3 and player2_point >= 3:
            return self.deuce()
        return f"{self.score(player1_point)} - {self.score(player2_point)}"

    def deuce(self):
        player1Name = self.player1.get_name()
        player2Name = self.player2.get_name()
        score = self.player1.get_point() - self.player2.get_point()
        if score == 0:
            return "Deuce"
        if score == 1:
            return f"Advantage {player1Name}"
        if score == 2:
            return f"Winner is {player1Name}"
        if score == -1:
            return f"Advantage {player2Name}"
        if score == -2:
            return f"Winner is {player2Name}"

    def score(self, point):
        if point == 0:
            return "Lover"
        if point == 1:
            return "Fifthteen"
        if point == 2:
            return "Thirty"
        if point == 3:
            return "Fourty"