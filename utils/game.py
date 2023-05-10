import random

class Hangman:
    def __init__(self):
        """Variables to be used for the methods are assigned under init constructor."""
        self.possible_words=['becode', 'learning', 'mathematics', 'sessions']
        #In order to be able to replace guessed letters, the word is cpnverted into a list each element being a letter.
        self.word_to_find= list(random.choice(self.possible_words))
        self.lives=5
        self.correctly_guessed_letters=(len(self.word_to_find)*["_"])
        self.wrongly_guessed_letters=[]
        self.turn_count=0
        self.error_count=0

    def play(self):
        """
        Method for asking the player to enter a letter. 
        If the player guessed a letter well, it will be added to `correctly_guessed_letters`. 
        If not, it will be added to the `wrongly_guessed_letters` and `error_count` will be incremented.
        """
        letter=input("Please enter a letter: ")
        # If-else condition in order to ensure that the player's input is a single alphabetical character.
        if letter.isalpha()==True and len(letter)==1:           
            # If the letter given by the player is true, a list of indices is generated contaning the index number of input letter. 
            # Then, a loop is created to replace the input with the right index in correctly guessed letters.
            if letter in self.word_to_find:
                indices=[index for (index,item) in enumerate(self.word_to_find) if item==letter]
                for i in indices:
                    self.correctly_guessed_letters[i]=letter
            # If the letter given is wrong, it is added to the list and relevant counts of error and life are adjusted.    
            else:
                self.wrongly_guessed_letters.append(letter)
                self.error_count+=1
                self.lives-=1
            self.turn_count+=1
            print(" ".join(self.correctly_guessed_letters).upper()) # Join method is used to print the letters not in a list of strings.
            print("remaining lives: ",self.lives)
            print("bad guessed letters: ",self.wrongly_guessed_letters)
            print("error count: ",self.error_count)
            print("turns: ",self.turn_count)
        else:
            if letter.isalpha()==False:
                print("Wrong input! You entered a non-alphabetical character.")
            elif len(letter)>1:
                print("Wrong input! You need to enter only one letter.")

    def game_over(self):
        """Method that will end the game when remaining lives is 0."""
        joined_word="".join(self.word_to_find).upper() # Asssigned a new variable to write it in f-string in below line.
        print(f"Game over...The correct word was {joined_word}!")

    def well_played(self):
        """
        Method that will end the game when player guessed 
        all the letters before lives are exhauseted.
        """
        joined_word="".join(self.word_to_find).upper() # Asssigned a new variable to write it in f-string in below line.
        print(f"You found the word:  {joined_word} in {self.turn_count} turns with {self.error_count} errors!")

    def start_game(self):
        """
        Method that will start the game and ensure the player to play 
        until the word is completeley guessed or the game is over.
        """
        while True:
            self.play()
            if self.lives ==0:
                self.game_over()
                break
            elif self.word_to_find==self.correctly_guessed_letters:
                self.well_played()
                break

play=Hangman()
play.start_game()
