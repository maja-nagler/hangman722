import random

word_list = ["banana", "cherry", "blueberry", "mango", "apple"]

word = random.choice(word_list)


import random

# Step 1: Create a while loop with a True condition
while True:
    # Step 2: Ask the user to guess a letter
    guess = input("Please enter a single letter:")

    # Step 3: Check if the guess is a single alphabetical character
    if len(guess) != 1 or guess.isalpha() == False:
         print("Invalid letter. Please, enter a single alphabetical character.")

    else :

        # Step 1: Check if the guess is in the word
        if guess in word:
            # Step 2: If the guess is in the word, print a success message
            print(f"Good guess! {guess} is in the word.")
        else:
            # Step 3: If the guess is not in the word, print a failure message
            print(f"Sorry, {guess} is not in the word. Try again.")
        
        # Break out of the loop
        break

