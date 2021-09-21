player -> server, receiver
score -> 0, 15, 30, 40, ADV, WIN

class Score:
    self.score = [0,15,30,40,45]

class Player:
    def __init__(self, name):
        self.name = name
        self.point = 0

    def get_player_score():
        return Score.score[self.point]
    
    def add_point():
        self.point++


class Scorer:
    def __init__(self,player1, player2):
        self.player1 = player1
        self.player2 = player2
    def get_score():
        if self.player1.get_player_score()= 45:
            return "Winner is A"
        if self.player2.get_player_score() == 45:
            return "Winner is B"
        if self.player1.get_player_score() == 40 and self.player2.get_player_score() == 40:
            return "deuce"
        else:
            return f"{self.get_point(self.player1.get_player_score())} - {self.get_point(self.player2.get_player_score())}"

    def get_point(point):
        if point == 15 :
            return "Fiffteen"

a = Player("A")
b = Player("B")

a.get_point()
a.get_point()

test_1:
    expected = "Deuce"
    a = Player("A")
    b = Player("B")
    scorer = Scorer(a,b)
    scorer.get_score()



แบ่ง test เป็น server win, receiver win

Testcase:
server get first point:
    - server score = 15
    - receiver score = 0
server get second point:
    - server score = 30
    - receiver score = 0
server get third point:
    - server score = 40
    - receiver score = 0
server win:
    - server score = 45
    - receiver score = 0   
receiver get first point:
    - receiver score = 15
    - server score = 0
receiver get second point:
    - receiver score = 30
    - server score = 0
receiver get third point:
    - server score = 40
    - receiver score = 0
receiver win:
    - receiver score = 45
    - server score = 0
deuce:
    - server score = 40
    - receiver score = 40
server Advantage:
    - server score = ADV
    - receiver score = 40
server win:
    - server score = win
    - receiver score = 40
receiver Advantage:
    - receiver score = ADV
    - server score = 40
receiver win:
    - receiver score = win
    - server score = 40

