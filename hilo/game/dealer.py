from game.player import Player
import random

class Dealer:
    """ A code template for the person that deals cards to the player.
    The responsibility of this class object is deal cards to the player. 
    
    Attributes:
        keep_playing (boolean): Whether the player wants to continue playing.
        firstCard (integer): An integer representing the first shown card.
        isHi (boolean): Represents if the player chose 'high' or not.
        player (Player): An instance of a class of objects known as Player.
    """
  
    def __init__(self):
        """Class constructor.
        
        Args:
            self (Dealer): An instance of Dealer
        """
        self.keep_playing = True
        self.firstCard = 0
        self.isHi = True
        self.player = Player()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing and self.player.can_play():
            self.firstCard = self.get_card()
            print(f"The card is: {self.convert_to_card(self.firstCard)}")
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            print() # For aesthetic reasons

    def get_inputs(self):
        """Gets the input after each round.
        
        Args:
            self (Dealer): An instance of Dealer"""
        if self.higher_or_lower() == 'h':
            self.isHi = True
        else:
            self.isHi = False
        

    def higher_or_lower(self):
        """Asks the player if they would like to guess higher or lower.
        
        Args:
            self (Dealer): An instance of Dealer"""
        choice = input("Higher or lower? [h/l] ").lower()
        if choice == 'h' or choice == 'l':
            return choice
        print("Invalid input.")
        return self.higher_or_lower()

    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Dealer): An instance of Dealer.
        """
        self.secondCard = self.get_card()
        if self.secondCard == self.firstCard:
            pass # If it is a tie, do nothing.
        elif self.secondCard > self.firstCard and self.isHi:
            self.player.get_points(True)
        elif self.secondCard < self.firstCard and not self.isHi:
            self.player.get_points(True)
        else:
            self.player.get_points(False)


    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the player guessed high or low and the points
        associated with that.

        Args:
            self (Dealer): An instance of Dealer.
        """
        print(f"Next card was: {self.convert_to_card(self.secondCard)}")
        print(f"Your score is: {self.player.points}")
        self.keep_playing_prompt()


    def get_card(self):
        """Returns a number representing a card value.

        Args:
            self (Dealer): An instance of Dealer.
        """
        return random.randrange(1,13)

    def keep_playing_prompt(self):
        """Asks the player if they would like to continue playing.

        Args:
            self (Dealer): An instance of Dealer.
        """
        if self.player.can_play():
            choice = input("Keep playing? [y/n] ").lower()
            if choice == 'n':
                self.keep_playing = False
            elif choice == 'y':
                self.keep_playing = True
            else:
                print("Invalid input.")
                self.keep_playing_prompt()
        else:
            print("Sorry, you lost. Game over.")

    def convert_to_card(self, num):
        """Converts a card value to a character representative of the face card.

        Args:
            self (Dealer): An instance of Dealer.
        """
        if num == 1:
            return 'A'
        elif num == 11:
            return 'J'
        elif num == 12:
            return 'Q'
        elif num == 13:
            return 'K'
        else:
            return num