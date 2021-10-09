from game.player import Player
import random

class Dealer:
  """ A code template for the person that deals cards to the player.
    The responsibility of this class object is deal cards to the player. 
    
    Attributes:
        new_card (boolean): Whether the player wants a new card or not
        score (number): Number of points earned
        player (Player): An instance of a class of objects known as Player.
    """
  
    def __init__(self):
      """Class constructor.
        
        Args:
            self (Dealer): An instance of Dealer
        """
      
        self.keep_playing = True
        self.new_card = True
        self.score = 300
        self.player = Player()

    def start_game(self):
      """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.firstCard = self.get_card
            print(f"The card is: {self.firstCard}")
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
      """Gets the input after each round.
        
        Args:
            self(Dealer): An intance of Dealer"""
        pass

    def do_updates(self):
      """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Director): An instance of Dealer.
        """
        pass

    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the player guessed high or low and the points
        associated with that

        Args:
            self (Director): An instance of Director.
        """
        pass

    def higher_or_lower(self):
        pass

    def get_card(self):
        # Returns a card between 1 - 13
        return random.randrange(1,13)
