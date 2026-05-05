import os


class HighScore:
  def __init__(self):
    self.high_score = 0
    os.makedirs("data", exist_ok=True)

    try:
      with open("data/high_score.txt", mode="x") as f:
        f.write("0")
    except FileExistsError:
      with open("data/high_score.txt", mode="r") as f:
        self.high_score = int(f.read())
  
  def update(self,score):
    if score > self.high_score:
      with open("data/high_score.txt", mode="w") as f:
        f.write(str(score))
      self.high_score = score