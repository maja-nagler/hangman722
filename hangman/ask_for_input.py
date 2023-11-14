# Step 1:
# Define a function called ask_for_input.
def ask_for_input():
# Step 2:
# Move the code that you wrote in the Iteratively check if the input is a valid guess task into this function block.

# Step 3:
# Outside the while loop, but within this function, call the check_guess function to check if the guess is in the word. Don't forget to pass in the guess as an argument to the method.

# Step 4:
# Outside the function, call the ask_for_input function to test your code.

    while True:

        guess = input("Please enter a single letter:")

        if len(guess) != 1 or guess.isalpha() == False:
            print("Invalid letter. Please, enter a single alphabetical character.")
        
        elif guess in self.list_of_guesses:
                print("You already tried that letter!")

        else:
            check_guess(guess)
            break
    
ask_for_input()


