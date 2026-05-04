from turtle import Turtle

GAME_OVER_HEIGHT = 120
GAME_OVER_SIZE = 50
MESSAGE_1_HEIGHT = -20
MESSAGE_2_HEIGHT = -50
MESSAGE_SIZE = 25

class Gameover (Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()

  def display(self):
    self.penup()
    self.speed("fastest")
    self.goto(0,GAME_OVER_HEIGHT)
    self.color("red")
    self.write("GAME OVER",move=False,align="center",font=("Arial", GAME_OVER_SIZE, "normal"))
    self.color("yellow")
    self.goto(0,MESSAGE_1_HEIGHT)
    self.write("Press 'r' to replay",move=False,align="center",font=("Arial", MESSAGE_SIZE, "normal"))
    self.goto(0,MESSAGE_2_HEIGHT)
    self.write("Click anywhere to exit",move=False,align="center",font=("Arial", MESSAGE_SIZE, "normal"))