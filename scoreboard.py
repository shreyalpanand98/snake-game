from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(270)
        self.curr_score = 0
        self.write_score()

    def write_score(self):
        self.write(f"score: {self.curr_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.sety(0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.curr_score += 1
        self.write_score()
