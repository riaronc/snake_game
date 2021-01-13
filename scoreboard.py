from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.score_update()

    def score_update(self):
        self.score += 1
        self.clear()
        self.write("Score = " + str(self.score), move=False, align=ALIGN, font=FONT)

    def end_game(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGN, font=FONT)
