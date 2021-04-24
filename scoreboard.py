from turtle import Turtle

ALIGNMENT = ["left", "right", "center"]
FONT = ('Courier', 80, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(arg=self.l_score, move=False, align=ALIGNMENT[2], font=FONT)
        self.goto(100, 200)
        self.write(arg=self.r_score, move=False, align=ALIGNMENT[2], font=FONT)

    def increase_right_score(self):
        self.clear()
        self.r_score += 1
        self.update_scoreboard()


    def increase_left_score(self):
        self.clear()
        self.l_score += 1
        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", move=False, align=ALIGNMENT, font=FONT)
