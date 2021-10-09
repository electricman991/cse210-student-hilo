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

        if self.points < 0:
            self.points = 0
        
        return self.points
    
    def can_play(self):
        if self.points > 0:
            return True
        return False
