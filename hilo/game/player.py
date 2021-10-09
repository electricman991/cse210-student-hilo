import random

class Player:
    """A code template for a person who guesses high or low. The responsibility of this
    class of objects is to say high or low, keep track of the values, the score, and 
    determine whether or not it can throw again."""


    def __init__(self):
        self.cards = 0
        self.points = 300
        self.firstCard = self.get_card()

    def get_points(self, wasCorrect):
        if wasCorrect == 'y':
            self.points += 100
        elif wasCorrect == 'n':
            self.points -= 75

        return self.points

    def higher_or_lower(self):
        first_card = self.get_card()
        print(f"\nThe card is: {first_card}")
        user_input = input(f'Higher or lower? [h/l] ')
        new_card = self.get_card()
        print(f'The new card is {new_card}')
        if user_input == 'h' and new_card > first_card:
            return self.get_points('y')
        elif user_input == 'h' and new_card < first_card:
            return self.get_points('n')
            
        elif user_input == 'l' and new_card < first_card:
            return self.get_points('y')
        else:
            return self.get_points('n')

        
        

    def get_card(self):
        # Returns a card between 1 - 13
        return random.randrange(1,13)
    
    def can_play(self):
        if self.points > 0:
            return True
        return False

    
            

