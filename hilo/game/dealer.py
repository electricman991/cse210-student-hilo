from game.player import Player

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
        self.keep_playing = 'y'
        self.player = Player()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing == 'y':
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
    
    
    
    def get_inputs(self):
        """Gets the input after each round.
        
        Args:
            self(Dealer): An intance of Dealer"""
        
        self.player.get_card()


    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Director): An instance of Dealer.
        """
        
        return self.player.points

            
        


    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the player guessed high or low and the points
        associated with that

        Args:
            self (Director): An instance of Director.
        """
        if self.player.can_play():
            self.player.higher_or_lower()
            print(f'Your score is: {self.player.points}')
            self.keep_playing = input('Keep playing? [y/n]: ')
        else:
            self.new_card = False
            print(f'Your score is: {self.score}')
            print('Game over')


        
        
