# Create your Phrase class logic here.

class Phrase:

    # dunder initializer
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        
    # method that prints out phrase to console with guessed letters visible and unguessed letters as underscores
    def display(self, guesses):
        for letter in self.phrase:
                if letter in guesses:
                    # prevent new line from being generated with each letter and underscore print
                    # https://stackoverflow.com/questions/11266068/python-avoid-new-line-with-print-command
                    print(letter, end=" ")
                else:
                    print("_", end=" ")

	  # method that checks if letter selected by user is in the phrase
    def check_letter(self, letter_guess):
		
		    # check if guessed letter is more than one letter
		    if len(letter_guess) > 1:
			      print("\nYour guess exceeds a single letter.")
			      return False
		
		    # check if guessed letter is actually a number instead; isnumeric function obtained from below link:	
		    # https://www.w3schools.com/python/ref_string_isnumeric.asp
		    elif letter_guess.isnumeric() == True:
			      print("\nYour guess is a number, not a letter.")
			      return False

		    # catch all other non-single letter letter guesses
		    elif letter_guess.isalpha() == False:
			      print("\nYour guess is invalid.")
			      return False

		    else:
			      return letter_guess in self.phrase

    # method that checks if whole phrase has been guessed. while the full phrase has not yet been guessed, method will return false. otherwise, it will return true
    def check_complete(self, guessed_letters):

		    # loop through each letter in phrase. if letter is not in user's guessed letters, return false
		    for letter in self.phrase:
			      if letter not in guessed_letters:
				        return False

        # once call to check_complete method bypasses for loop (all letters in phrase have been guessed), return true
		    return True
