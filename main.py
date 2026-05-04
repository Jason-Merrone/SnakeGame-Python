from turtle import Screen
from game_state import GameState


def start_game():
  screen = Screen()
  screen.setup(width=600,height=600)

  gamestate = GameState(screen)
  gamestate.initialize()
               
  gamestate.run()
  screen.mainloop()

start_game()