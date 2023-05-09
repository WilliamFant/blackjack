# first import logo from art .py
from art import logo

import os
import random


def clear():
    """clears the console across operating system"""
    command = 'clear'
    if os.name == ('nt', 'dos'):
        command = 'cls'
        # inputs the command variable into the system function from the os module this exicutes the command in the console
        os.system(command)


def deal_card():
    """this returns a random card from the list"""
    # create a card list that has a through 10
    # all royals are 10
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # use the random Module with the choice
    card = random.choice(cards)
    return card

# score cards


def calculate_score(cards):
    """Take a list of cards and returns the score calculated from the cards"""
    # create an if statement if the player has blackjack
    if sum(cards) == 21 and len(cards) == 2:
        # return 0 to represent our blackjack we will use this instead of 21 to show difference from 21
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def play_game():
    def compare(user_score, computer_score):
        """pass in user score and computer score as arguments"""
        if user_score == computer_score:
            return "draw"
        elif computer_score == 0:
            # cpu_wins = cpu_wins + 1
            return "L computer has blackjack"
        elif user_score == 0:
            # user_wins = user_wins + 1
            return "W with blackjack"
        elif user_score > 21:
            # cpu_wins = cpu_wins + 1
            return "You went over you lose"
        elif computer_score > 21:
            return "Cpu went over you win"
        elif user_score > computer_score:
            # user_wins = user_wins + 1
            return "You win"
        else:
            # cpu_wins = cpu_wins + 1
            return "You lose"
    """this function will run when the game begins"""
    print(logo)

    user_cards = []
    computer_cards = []
    # create a variable to notate weather or not the game should continue
    is_game_over = False
    # blackjack starts with 2 cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        # using calculate score option
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        # using print statments have the current score
        print(f"your cards {user_cards}, current score {user_score}")
        print(f"computers first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # create an input to hit or stand
            user_should_deal = input(
                "Type 'y' to get another card (hit), type 'n' to stand: ")
            if user_should_deal.lower() == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # have print statments and f strings that print out the user score and computer score
    print(f"Your final hand: {user_cards} Your final score: {user_score}")
    print(
        f"Computer final hand: {computer_cards} Computer final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Want to play blackjack 'y' or 'n': ").lower() == 'y':
    clear()
    play_game()

# user wins displays after the logo print statement needs to be defined and added if the user wins and if the cpu winscd
