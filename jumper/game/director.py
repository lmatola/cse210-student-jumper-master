from game.console import Console
from game.puzzle_parachute import Puzzle_Parachute
from game.puzzle_word import Puzzle_Word

class Director:
    

    def __init__(self):
        
        self.Console = Console()
        self.Puzzle_parachute = Puzzle_Parachute()
        self.Keep_playing = True
        self.Puzzle_word = Puzzle_Word()
        self.User_letter = ""
        
    def start_game(self):
        
        while self.keep_playing:
            self.do_outputs()
            self.get_inputs()
            self.do_updates()
            
    def do_outputs(self):

        self.Puzzle_word.draw_word_blank()
        self.Puzzle_parachute.draw_parachute()

    def get_inputs(self):
        
        self.user_letter = self.Console.read("Guess a letter [a-z]: ")

    def do_updates(self):
        

        correct_guess = self.Puzzle_word.process_guess(self.user_letter)
        if correct_guess == False:
            self.Puzzle_parachute.remove_parachute_piece()

        if self.Puzzle_word.keep_playing() == True:
            if self.Puzzle_parachute.keep_playing() == True:
                self.Keep_playing == True
            else:
                self.Keep_playing = False
                self.Puzzle_parachute.change_parachute_gone()
                self.Puzzle_parachute.draw_parachute()
        else:
            self.Keep_playing = False