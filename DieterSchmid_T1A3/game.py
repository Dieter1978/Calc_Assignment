import random

class Game:
    def __init__(self):
        self.number = random.randint(1,10)
    

    def __call__(self, guess):

          if guess > self.number:
                return "Lower!"
          elif guess < self.number:
                return "Higher!"
          else:
                self.number = random.randint(0,10)
                return "You guess it!"