from game.player import Player

class Dealer:
    """ A code template for the person that deals cards to the player.
    The responsibility of this class object is deal cards to the player. 
    
    Attributes:
        new_card (boolean): Whether the player wants a new card or not
        score (number): Number of points earned
        player (Player): An instance of a class of objects known as Player.
    """

    def __int__(self):
        """Class constructor.
        
        Args:
            self (Dealer): An instance of Dealer
        """
        self.new_card = True
        self.score = 300
        self.player = Player()

    def start_game():
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
    
    
    
    def get_inputs():
        """Gets the input after each round.
        
        Args:
            self(Dealer): An intance of Dealer"""


    def updates_score(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Director): An instance of Dealer.
        """

    def outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the player guessed high or low and the points
        associated with that

        Args:
            self (Director): An instance of Director.
        """
