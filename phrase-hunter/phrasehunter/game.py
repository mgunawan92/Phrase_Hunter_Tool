# Create your Game class logic in here.
import random
from phrasehunter.phrase import Phrase


class Game:
    
    
    def __init__(self):
        # initialized to 0 per requirements
        self.missed = 0
        
        # set phrases; all phrases property of MGM - 007 SPECTRE
        self.phrases = [Phrase("A license to kill is also a license to not kill"),
                        Phrase("I always knew death would wear a familiar face"),
                        Phrase("You are a kite dancing in a hurricane"),
                        Phrase("Shaken not stirred"),
                        Phrase("Well it was that or the priesthood"),]
        
        # initialize active phrase to None per the requirements
        self.active_phrase = None
        
        # initialize list of previous guesses per requirements
        self.guesses = [" "]
        

    def start(self):
        
        # get phrase from get random phrase method
        self.get_random_phrase()

        # display welcome message
        self.welcome()
    
        # loop that verifies if maximum number of 5 guesses has not been reached and run check_complete method to verify that all letters in phrase has not been guessed yet (False)
        while self.missed < 5 and self.active_phrase.check_complete(self.guesses) == False:
    
    		# update the user on how many incorrect guesses they have entered, and how many they have remaining
            print("\nYou have entered {} incorrect guesses\n".format(self.missed))
            print("You have {} out of 5 guesses remaining\n".format(5-self.missed))
    
            # pass the randomly selected phrase along with the current list of all guessed letter. print out phrase with previously-guessed correct letters visible, all others as underscore
            Phrase.display(self.active_phrase, self.guesses)
    
            # get guess from user
            letter_guess = self.get_guess()
            
            #add guessed letter to guesses list
            self.guesses.append(self.letter_guess)
    
            # check if user's guessed letter is in phrase. if not, add additional count to missed
            if self.active_phrase.check_letter(letter_guess) == False:
                self.missed += 1
    
            # run game over each time to determine if maximum number of guesses has been reached
            self.game_over()
            
        self.play_again()
            

    def get_random_phrase(self):
        
	      # set active phrase as one of the randomly selected five phrases
        self.active_phrase = random.choice(self.phrases)
        return self.active_phrase
                    
            
    def welcome(self):
        
	      print("Welcome to Phrase Hunter! ")
        

    def get_guess(self):
    
        # prompt user for guess
		    self.letter_guess = input("\n\nGuess a letter; anything other than a single letter will count against your guesses. ")

		    return self.letter_guess


    def game_over(self):

		    # verify if 5 guesses have been made, in which case, print Game Over message
		    if self.missed == 5:
		        print("\nYou've reached the max of 5 incorrect guesses. Game Over!\n")

		    # if 8 guesses has not yet been reached, run check_complete method to see if all letters have been guessed (True). If call returns True, print out victory message
		    elif self.active_phrase.check_complete(self.guesses) == True:
		        print("\nCongratulations, you guessed the full phrase!\n")
            
            
    def play_again(self):
        
        proceed = True
        
        while proceed == True:
            
            self.response = input("Play another game? (Y/N) ")
            self.response = self.response.lower()
        
            if self.response == "y":
                
                # re-initialize number of incorrect guesses to 0
                self.missed = 0
                
                # re-initialize phrase to None
                self.active_phrase = None
                
                # re-initialize list of previous guesses
                self.guesses = [" "]
                
                # restart game
                return self.start()
            
            elif self.response == "n":
                
                print("Thanks for Playing\n")
                proceed = False
                
            else:
                
                print("That isn't a valid response. Please enter y or n.")
                proceed == True