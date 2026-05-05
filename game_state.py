from turtle import Screen
from snake import Snake
from apple import Apple
from score import Score
from gameover import Gameover

GAME_SPEED = 75 # ms 
class GameState:
  def __init__(self, screen: Screen):
    self._screen=screen
    self._snake = None
    self._score = None
    self._game = None
    self._gameover = None
    self._id = 0

  def run(self):
    self._game_loop(self._id)
  
  def _game_loop(self, session):
    if session != self._id:
      return
    
    self._screen.update()
    self._score.update_screen()

    if self._snake.collide_with_apple(self._apple):
        self._score.increase_score()
    
    if self._snake.move():
      self._screen.ontimer(lambda: self._game_loop(session),GAME_SPEED) 
    else:
      self._score.update_high_score()
      self._gameover.display()
      self._screen.onscreenclick(lambda x, y: self._screen.bye())

  def initialize(self):
    self._id += 1
    self._screen.clear()
    self._screen.bgcolor("black")
    self._screen.title("My Snake Game")
    self._screen.tracer(0)
    self._snake = Snake(self._screen.window_width(), self._screen.window_height())
    self._apple = Apple(self._snake, self._screen.window_width(), self._screen.window_height())
    self._gameover = Gameover()
    self._score = Score()

    # Keypress logic
    self._screen.listen()
    self._screen.onkey(self._snake.up, "Up")
    self._screen.onkey(self._snake.down, "Down")
    self._screen.onkey(self._snake.left, "Left")
    self._screen.onkey(self._snake.right, "Right")
    self._screen.onkey(self.reset, "r")
    
  def reset(self):
    self.initialize()
    self.run()