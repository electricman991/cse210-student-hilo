import random

class Player:
  """A code template for a person who guesses high or low. The responsibility of this
    class of objects is to say high or low, keep track of the values, the score, and 
    determine whether or not it can throw again."""

    def __init__(self):
        self.points = 300

    def get_points(self, wasCorrect):
        if wasCorrect:
            self.points += 100
        else:
            self.points -= 75

        return self.points

    def higher_or_lower(self):
        # Returns True if a Hi was played, False if a Lo was played

    def get_card(self):
        # Returns a card between 1 - 13
        return random.randrange(1,13)
    
    def can_play(self):
        if self.points > 0:
            return True
        return False
