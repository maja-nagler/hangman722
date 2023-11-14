#The check_guess function will take the guessed letter as an argument and check if the letter is in the word.

#Step 1:
#Define a function called check_guess. pass in the guess as a parameter for the function.
#Write the code for the following steps in the body of this function.

def check_guess(guess):
    guess = input("Please enter a single letter:")
#Step 2: Convert the guess into lower case.
    guess = guess.lower()
#Step 3: Move the code that you wrote to check if the guess is in the word into this function block.


    if guess in word:
    #In the body of the if statement, print a message saying "Good guess! {guess} is in the word.". Obviously, format the string to show the actual guess instead of {guess}.
        print(f"Good guess! {guess} is in the word.")

    #Create an else block that prints a message saying "Sorry, {guess} is not in the word. Try again." This block of code will run if the guess is not in the word.
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")