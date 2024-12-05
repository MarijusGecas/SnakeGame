from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 370)
        self.color("white")

    def display_score(self, score):
        self.clear()
        self.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 16, "normal"))