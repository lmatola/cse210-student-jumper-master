
import random

new_list = []


# open the file
with open("wordlist.txt") as file:
    #read the line
    for line in file.readlines():
        # Split the line into words
        for word in line.split("\n"):   
            #Check each word's length and add to the privided list.
            if len(word) == 5:
                new_list.append(word)


class puzzle_word:

    """
    Game begins from the guess. Guess includes game menu and receives input from the user.
    It is the main class to call other classes.
    """

    def __init__(self, new_list):
        """
        It enables the random selection/choice of the words from list 'new_list'.

        """
        word_random = random.SystemRandom()
        word_chosen = word_random.choice(new_list)
        self.word_chosen = word_chosen

    def game_begin(self):
                
        """
        Function game_begin is the main function which enables the game, store inputs from user,
        give feedback for each input from the user.

        """
        option = " "
        incorrect_letter_try = 0
        print()
        print("**************************")
        print("WELCOME TO THE JUMPER GAME")
        print("**************************")
        counter_w = 0
        while option != "q" :
            word_ch = self.word_chosen
            print(word_ch)
            word_ch = word_ch.lower()
            letters = []
            letters_used = []
            letters.clear()
            for letter in word_ch:
                letters.append(letter)
            incorrect_guess = 0
            gave_up = 0
            letters_trial = 0
            incorrect_letter_try = 0
            counter_w = counter_w + 1
            print("\n-------------------------")
            print("GUESS THE FIVE WORDS!")
            print("-------------------------")

            c_guess = ["- ","- ","- ","- ","- "]
            
            guess_letter = ""
            for w in c_guess:
                guess_letter = guess_letter+w
            print("\n\nCurrent Guess: " + guess_letter)
            print("\n  _____ \n /_____\ \n \     / \n  \   /  \n    0 \n   /|\ \n   / \ \n \n^^^^^^^\n") # this line difines the parachute
            Keep_playing = True
            while Keep_playing == True:
                menu = "\ng = PLAY THE GAME OR q = QUIT, ENTER YOUR CHOICE: " # the player chose to play the game or quit.
                
                option = input(menu).lower()
 
                if option == "g":
                    letter_entered = input("\nGuess a letter [a-z]: ").lower() # the player guess the letter from the hidden chosen word.
                    
                    if letters_used.count(letter_entered) == 0:
                        if len(letter_entered) == 1:
                            letters_trial = letters_trial + 1  # total no. of letter trials
                            letter_found = False
                            count_found = 0
                            c_guess_prev = ""
                            for q in c_guess:
                                c_guess_prev = c_guess_prev + q
                            for let in range(0,len(letters)):
                                if letters[let] == letter_entered:
                                    letter_found = True
                                    count_found = count_found + 1
                                    c_guess[let] = letter_entered
                            if letter_found == True:
                                letters_used.append(letter_entered)
                                guess_letter = ""
                                for w in c_guess:
                                    guess_letter = guess_letter + w
                                if guess_letter != word_ch:
                                    if count_found == 1:
                                        print("\n\nFEEDBACK: Great guess! You found 1 letter!")
                                    if count_found > 1:
                                        print("\n\nFEEDBACK: Bravo! You found " + str(count_found) + " letters!")
                                    print("\nCurrent Guess: " + guess_letter)
                                if guess_letter == word_ch:
                                    print("\n\nFEEDBACK: Well done! You discovered the entire word! \n")
                                    print("The word is: " + word_ch.upper())
                                    gave_up_guess = 0
                                    quit_guess = 0

                            else:
                                incorrect_letter_try = incorrect_letter_try + 1 #total no. of incorrect trials
                                if incorrect_letter_try == 1:
                                    print("\nCurrent Guess: " + guess_letter)
                                    print("\n /_____\ \n \     / \n  \   /  \n    0 \n   /|\ \n   / \ \n \n^^^^^^^") # this line difines the parachute when the player guesses wrong at first time.

                                elif incorrect_letter_try == 2:
                                    print("\nCurrent Guess: " + guess_letter)
                                    print("\n \     / \n  \   /  \n    0 \n   /|\ \n   / \ \n \n^^^^^^^")# this line difines the parachute when the player guesses wrong at second time.

                                elif incorrect_letter_try == 3:
                                    print("\nCurrent Guess: " + guess_letter)
                                    print("\n  \   /  \n    0 \n   /|\ \n   / \ \n \n^^^^^^^")# this line difines the parachute when the player guesses wrong at third time.

                                elif incorrect_letter_try == 4:
                                    Keep_playing = False
                                    print("\n\nCurrent Guess: " + guess_letter)
                                    print("\n    x \n   /|\ \n   / \ \n \n^^^^^^^")# this line difines the parachute when the player guesses wrong at fourth time.
                                    print("GAME OVER")

                                    
                                else:
                                    print("\n\nFEEDBACK: No letter found! Try again mate!")
                                    print("\nCurrent Guess: " + guess_letter)
                        else:
                            print("\n\nFEEDBACK: You are supposed to enter one letter only!")
                            print("\nCurrent Guess: " + guess_letter)
                    else:
                        print("\n\nFEEDBACK: You have already found this letter, Try a different letter!")
                        print("\nCurrent Guess: " + guess_letter)
                   

                elif option == "q":
                    quit_guess = 1
                    Keep_playing = False
                    print("\nThank you for playing The Jumper Game!")
                    print()

                else:
                    print("\n \n Not a correct option! Choose again!")

puzzle_word(new_list).game_begin()
