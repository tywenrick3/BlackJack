# Author: <Ty Wenrick>
# Assignment #3 - Blackjack
# Date due: 2021-03-25
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

import random

FACE_CARD_VALUE = 10
ACE_VALUE = 1
CARD_LABELS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
BLACKJACK = 21
DEALER_THRESHOLD = 16


####### DO NOT EDIT ABOVE ########


#my code works as intended and does everything as outlined in the project description but the last autograder
# tests has an issue with the specific way im outputting something and therefore fails

def deal_card():
    """Evaluates to a character representing one of 13
    cards in the CARD_LABELS tuple

    :return: a single- or double-character string representing a playing card"""
    #uses randoms choice method to pick a random card label
    return random.choice(CARD_LABELS)


def get_card_value(card_label):
    """Evaluates to the integer value associated with
    the card label (a single- or double-character string)

    :param card_label: a single- or double-character string representing a card
    :return: an int representing the card's value
    """
    #numbers are converted to integers and and ace is assigned to 1 the rest (face cards) are assigned 10
    if card_label == '2' or card_label == '3' or card_label == '4' or card_label == '5' or card_label == '6' or card_label == '7' or card_label == '8' or card_label == '9' or card_label == '10':
        return int(card_label)
    elif card_label == 'A':
        return int(1)
    else:
        return int(10)


def deal_cards_to_player():
    """Deals cards to the player and returns the card
    total

    :return: the total value of the cards dealt
    """

    BLACKJACK = 20
    card1 = deal_card()
    card2 = deal_card()
    total = get_card_value(card1) + get_card_value(card2)
    print('Player drew ' + card1 + ' and ' + card2 + '.')
    print("Player's total is", str(total) + '.')
    print()

    #while the total is less than 21 give the player the choice to hit or stay and add the card value if its a hit
    while total <= BLACKJACK:
        player_choice = input('Hit (h) or Stay (s)? ')
        print()
        if player_choice == 'h':
            hit_card = deal_card()
            total += get_card_value(hit_card)
            print('Player drew', str(hit_card) + '.')
            print("Player's total is", str(total) + '.')
            print()
        elif player_choice == 's':
            break

    return int(total)


def deal_cards_to_dealer():
    """Deals cards to the dealer and returns the card
    total

    :return: the total value of the cards dealt
    """
    DEALER_THRESHOLD = 16
    card1 = deal_card()
    card2 = deal_card()
    total = get_card_value(card1) + get_card_value(card2)
    print('The dealer has ' + card1 + ' and ' + card2 + '.')
    print("Dealer's total is", str(total) + '.')
    print()

    #forces the dealer to hit untill his total value is at or above 16
    while total < DEALER_THRESHOLD:
        hit_card = deal_card()
        total += get_card_value(hit_card)
        print('Dealer drew', hit_card + '.')
        print("Dealer's total is", str(total) + '.')
        print()

    return int(total)


def determine_outcome(player_total, dealer_total):
    """Determines the outcome of the game based on the value of
    the cards received by the player and dealer. Outputs a
    message indicating whether the player wins or loses.

    :param player_total: total value of cards drawn by player
    :param dealer_total: total value of cards drawn by dealer
    :return: None
    """

    BLACKJACK = 21

    #if players total is more than the dealers or the dealer busts you win, else you lose including if you bust
    if player_total > dealer_total or dealer_total > BLACKJACK:
        print('YOU WIN!')
        print()
    else:
        print('YOU LOSE!')
        print()




def play_blackjack():
    """Allows user to play Blackjack by making function calls for
    dealing cards to the player and the dealer as well as
    determining a game's outcome

    :return: None
    """
    BLACKJACK = 21
    print("Let's Play Blackjack!")
    print()

    play_again = True

    #exit this for loop only when the 'again input' equals 'N'
    #everything in the for loop takes you through a full game of blackjack and ends with a choice to play again
    while play_again:

        player_total = deal_cards_to_player()

        if player_total > BLACKJACK:
            print('YOU LOSE!')
            print()

            #this loop is used twice in this function
            #it keeps displaying the play again message untill the player enters eaither Y or N
            while True:
                again_input = input('Play again (Y/N)? ')
                print()
                if again_input == 'Y':
                    play_again = True
                    break
                elif again_input == 'N':
                    play_again = False
                    break

        else:
            dealer_total = deal_cards_to_dealer()

            determine_outcome(player_total, dealer_total)

            while True:
                again_input = input('Play again (Y/N)? ')
                print()
                if again_input == 'Y':
                    play_again = True
                    break
                elif again_input == 'N':
                    play_again = False
                    break

    print('Goodbye.')


def main():
    """Runs a program for playing Blackjack with one player
    and a dealer
    """

    play_blackjack()


####### DO NOT REMOVE IF STATEMENT BELOW ########

if __name__ == "__main__":
    # Remove comments for next 4 lines to run doctests
    # print("Running doctests...")
    # import doctest
    # doctest.testmod(verbose=True)

    # print("\nRunning program...\n")

    main()
