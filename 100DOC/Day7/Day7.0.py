#Step 1
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
random_number = random.randint(0,len(word_list)-1)
random_word = word_list[random_number]
# print(random_word)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input('Guess a letter').lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in random_word:
    if letter == guess:
        print('Correct')
    else:
        print('wrong')
