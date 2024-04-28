import random

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card
#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.
def calculate_scores(scores):
    if sum(scores) == 21 and len(scores) == 2:
        return 0
    elif 11 in scores and  sum(scores) > 21:
        scores.remove(11)
        scores.append(1)
    return sum(scores)
def compare(user_scr, comp_scr):
    if user_scr == 0:
        print('you win, with a blackjack')
    elif comp_scr == 0:
        print('you loose, computer has a blackjack')
    elif user_scr > 21:
        print('you went out of bonds')
    elif comp_scr >21:
        print('computer went out of bounds')
    elif user_scr == comp_scr:
        print('draw')
    elif user_scr > comp_scr:
        print('you win')
    else:
        print('you loose')






start_game = True
while start_game == True:

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []
    game_ends = False
    for num in range(0, 2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while game_ends == False:
        user_score = calculate_scores(user_cards)
        computer_score = calculate_scores(computer_cards)

        if computer_score == 0 or user_score == 0 or user_score > 21:
             game_ends = True
        else:
            print(f'Your cards:{user_cards}, and your score:{user_score}')
            print(f'Computer\'s one card:{computer_cards[0]}')
            ask = input('Do you want to draw another card? Y or N?')
            if ask == 'y':
                user_cards.append(deal_card())
            else:
                game_ends = True
    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_scores(computer_cards)


    compare(user_score, computer_score)
    print(f'Your cards:{user_cards}, and your score:{user_score}')
    print(f'Computer cards:{computer_cards} and score:{computer_score}')

    play = input('Do you want to play Blackjack again?')
    if play == 'y':
        start_game = True
    else:
        start_game = False


















#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

