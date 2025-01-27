from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', mode='r') as f:
            self.high_score = int(f.read())
        self.color('white')
        self.penup()
        self.goto(0, 265)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # Replace the game_over method with a reset scoreboard.
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game over", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as f:
                f.write(f"{self.high_score}")
        # Don't place the following code before the if statement; otherwise, the score will
        # never be greater than the high score!
        self.score = 0
        self.update_scoreboard()

