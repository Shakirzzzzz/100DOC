#First generate a random number between 1 - 100
import random
random_number = random.randint(0,100)
print(random_number)


def compare(lives):
    if lives != 0:
        user_guess = int(input('Guess a number'))
        if user_guess == random_number:
            print('you won')
            print(random_number)
        else:
            lives -= 1
            if user_guess > random_number:
                print('wrong answer. Too High')
            else:
                print('wrong answer. Too low')

            print(f'lives:{lives}')
            compare(lives)
    else:
        print('you are out of lives')



#Give 5 or 10 chances depending on user input
lives = 0
mode = input('What mode do you want to play the game on? easy or hard?')
if mode == 'easy':
    lives = 10
    print(f'you get:{lives} lives')
else:
    lives = 5
    print(f'you get:{lives} lives ')






# start the guessing game with the chosen  number of lives

compare(lives)
#if guese is not equal to the guessed number  take 1 life away
#if guess is equal to the chosen number the player wins
