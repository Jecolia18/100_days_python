#Step 1 
import random
word_list = ["ardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = word_list[random.randint(0, 2)] #can use the random.choice() instead
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter in the chosen word: ").lower()
if len(guess) > 1:
    print("enter just one letter")
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
else:
    print(chosen_word)
    for i in chosen_word:
        if i == guess:
            print("correct letter")
        else:
            print("wrong guess")