import random
from data import data
import art




print(art.logo)


def players(choice, letter):
    name = choice['name']
    description = choice['description']
    country = choice['country']
    print(f'Choice{letter}:{name},  {description} from {country}')
game_play = True
score = 0
for i in range(0, 2):
    first_choice = random.choice(data)
    second_choice = random.choice(data)
if first_choice == second_choice:
    second_choice == random.choice(data)
scoreA = first_choice['follower_count']
scoreB = second_choice['follower_count']
while game_play == True:
    scoreA = first_choice['follower_count']
    scoreB = second_choice['follower_count']
    print(f'Score:{score}')
    players(first_choice, 'A')
    print(art.vs)
    players(second_choice, 'B')
    choice = input('Who has more followers? A or B?')
    if choice == 'A' and (scoreA > scoreB):
        score += 1
        print('Correct')
        print(f'A:{scoreA}')
        print(f'B:{scoreB}')


        second_choice = random.choice(data)
    elif choice == 'B' and (scoreA > scoreB):
        print('wrong answer')
        print(f'A:{scoreA}')
        print(f'B:{scoreB}')
        game_play = False





    elif choice == 'A' and (scoreA < scoreB):
        print('wrong answer')
        print(f'A:{scoreA}')
        print(f'B:{scoreB}')
        game_play = False

    elif choice == 'B' and (scoreA < scoreB):
        score += 1
        first_choice = second_choice
        second_choice = random.choice(data)
        print('Correct')
        print(f'A:{scoreA}')
        print(f'B:{scoreB}')

    elif choice == ('A' or 'B') and scoreA == scoreB:
        print('Bug')

    else:
        print('Type A or B, Bitch. Dont be a smartass')







