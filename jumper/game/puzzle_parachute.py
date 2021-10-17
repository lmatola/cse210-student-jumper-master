from game.console import Console

class Puzzle_Parachute:

    # TO DO Define the Puzzle_Parachute class
    """A code template for the puzzle parachute. The responsiblity of this class of
    is to display a parachute and the jumper.
    
    Sterotype: 
            Information Holder
    
    Attributes: 
            parachute (list): holds the parts for the parachute
            jumper (list): holds the parts for the jumper """

    def __init__(self): 
        """The class constructor.

        Args:
            self(Puzzle_Parachute): an instance of Puzzle_Parachute."""

        self.parachute = [" ___","/___\ ", "\   /", " \ /"]
        self.jumper = ["  0 "," /|\ ", " / \ "," ","^^^^^^^"]
        
    def draw_parachute(self):
        """ Draws / show the parachute and the jumper and the begining of the game.
        Args:
            self(draw_parachute): an instance of Puzzle_Parachute.  """

        for part in self.parachute: # for loops throught the parts/list in puzzle_parachute.parachute
            print (part) # print each part or each item in the list 
        for part in self.jumper: # for loops throught the part/list in in puzzle_parachute.jumper
            print (part) # prints each part/list in in puzzle_parachute.parachute

    def remove_parachute_piece(self):
        """ This method removes part of the parachute piece, it is only called if the input from correct_guess is false.
        Args: 
            self (remove_parachute_piece): an instance of Puzzle_Parachute."""

        self.parachute.pop(0) 
        # self.parachute uses pop to delete from the index set to zero so start from the begining instead the end.

    def keep_playing(self):
        """ This method is dependent on if the parachute is gone. If there are still parts of the parachute
            the player can keep playing
        Args: 
            self(keep_playing):     an instace of Puzzle_Parachute
            keep_playing(boolena):  whether or not the game can continue.
        Returns: boolean"""
        keep_playing = True # define boolean

        if len(self.parachute) == 0: # if the length of Puzzle_Parachute.parchute equals zero
            keep_playing = False     # keep playing will equal False

        return keep_playing          # return keep_playing

    def change_parachute_gone(self):
        """This method will change the 0 to an X if the parachute is gone 
        Args: 
            self(change_parachut_gone): an instace of Puzzle_Parachute"""
        self.jumper = ["  x "," /|\ ", " / \ "," ","^^^^^^^"] # change jumper from 0 to x



















      