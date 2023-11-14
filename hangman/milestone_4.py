
import random

word_list = ["banana", "cherry", "blueberry", "mango", "apple"]




class Hangman:
    """
    The hangman game.
    """
    def __init__(self, word_list, num_lives = 5):
        """
        Initialize the game with the word to guess.

        :type  word: str
        :param word: the word to guess.
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word = random.choice(word_list)
        letter_guessed = list(set(word))
        self.word_guessed = ['_' for i in self.word[i]]
        self.num_letters = len(set(self.word))


    def check_guess(guess):
        guess = guess.lower()

        for i in len(self.word):
            if guess in Hangman.word:
                print(f"Good guess! {guess} is in the word.")
                self.word_guessed[i] = guess
                num_letters = num_letters - 1

            else:
                print(f"Sorry, {guess} is not in the word. Try again.")
                num_lives = num_lives - 1
                print(f"You have {num_lives} lives left.")


    def ask_for_input():

        condition = Hangman.num_letters > 0 and Hangman.letter_guessed not in Hangman.list_of_guesses
        while condition == True:

            guess = input("Please enter a single letter:")

            if len(guess) != 1 and guess.isalpha() == False:

                print("Invalid letter. Please, enter a single alphabetical character.")
                
            
            elif guess in Hangman.list_of_guesses:
                print("You already tried that letter!")
            else:
                Hangman.check_guess(guess)
                Hangman.list_of_guesses.append(guess)
                break
                
Hangman.ask_for_input()
      