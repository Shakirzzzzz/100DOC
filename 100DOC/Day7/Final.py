import random
from hangman_words import word_list
from hangman_art import stages,logo



# generate a random word
chosen_word = random.choice(word_list)
# hint
print(chosen_word)
char_len = len(chosen_word)
print(logo)
# initial string of dashes and lives count
display = []

for i in range(char_len):
    display.append('_')
print(display)
lives = char_len
# game loop
end_of_game = False
while  not end_of_game:
    guess = input('Guess a letter')
    if guess in display:
        print('you have already guessed that')
    for j in range(char_len):
        letter = chosen_word[j]
        if guess == letter:
            display[j] = guess

    if guess not in chosen_word:
        lives -=1
        print(lives)
        print(stages[lives])
        print('Not the correct answer')
    

    if '_' not in display:
        end_of_game = True
        print('Congrats, you finished the game')
    if lives == 0:
        print('You are out of lives')
        end_of_game = True
    print(display)









