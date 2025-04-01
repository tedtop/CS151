"""
Main Blackjack game implementation.
Author: Ted Toporkov
Date: Dec 6, 2025
"""

from deck import Deck
from player import Player

def get_valid_bet_amount(player):
    """
    Prompts the user to enter a valid bet amount.

    Args:
        player (Player): The player object whose balance is checked.

    Returns:
        int: A valid bet amount.
    """
    while True:
        try:
            bet_amount = int(input("How much $ would you like to bet? "))
            if 0 < bet_amount <= player.get_balance():
                return bet_amount
            print("Invalid bet amount. Enter a number between 1 and your balance.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def deal_cards(player, dealer, deck):
    """
    Deals initial cards to player and dealer.

    Args:
        player (Player): The player object.
        dealer (Player): The dealer object.
        deck (Deck): The deck of cards.
    """
    player.deal_card(deck)
    dealer.deal_card(deck)
    player.deal_card(deck)
    dealer.deal_card(deck)

def print_initial_hands(player, dealer):
    """
    Prints initial hands with dealer's second card hidden.

    Args:
        player (Player): The player object.
        dealer (Player): The dealer object.
    """
    player.print_hand()
    dealer.print_hand(show_all=False)

def hit_or_stand(player, dealer, deck):
    """
    Manages player's turn of hitting or standing.

    Args:
        player (Player): The player object.
        dealer (Player): The dealer object.
        deck (Deck): The deck of cards.

    Returns:
        bool: True if player busts, False otherwise.
    """
    while True:
        response = input("Hit? [y]/n: ").lower().strip() or 'y'
        if response != 'y':
            print("\nYou stand.\n")
            return False

        print("\nHit!\n")
        player.deal_card(deck)
        player.print_hand()
        dealer.print_hand(show_all=False)

        if player.blackjack_hand_value() > 21:
            print("Bust!")
            return True

def dealer_play(dealer, player, deck):
    """
    Manages dealer's turn with soft 17 rule.

    Args:
        dealer (Player): The dealer object.
        player (Player): The player object.
        deck (Deck): The deck of cards.

    Returns:
        bool: True if dealer busts, False otherwise.
    """
    while dealer.blackjack_hand_value() < 17:
        print(f"Dealer hits on {dealer.blackjack_hand_value()}.\n")
        dealer.deal_card(deck)
        dealer.print_hand()
        player.print_hand()

        if dealer.blackjack_hand_value() > 21:
            print("Dealer busts!")
            return True

    print(f"Dealer stands on {dealer.blackjack_hand_value()}.\n")
    return False

def determine_winner(player, dealer, bet_amount):
    """
    Determines game outcome and updates player's balance.

    Args:
        player (Player): The player object.
        dealer (Player): The dealer object.
        bet_amount (int): The amount bet.
    """
    player_value = player.blackjack_hand_value()
    dealer_value = dealer.blackjack_hand_value()

    if player.blackjack():
        if dealer.blackjack():
            print("Push (both have Blackjack).")
        else:
            print("Blackjack! You win 3:2.")
            player.win(int(bet_amount * 2.5))
    elif player_value > 21:
        print("You bust!")
    elif dealer_value > 21:
        print("Dealer busts! You win!")
        player.win(bet_amount * 2)
    elif player_value > dealer_value:
        print("You win!")
        player.win(bet_amount * 2)
    elif player_value < dealer_value:
        print("Dealer wins.")
    else:
        print("Push (tie).")

def main():
    """
    Main game loop for Blackjack.
    """
    # Get the player's name and initial balance
    while True:
        player_name = input("What is your name? ")
        if player_name.isalnum():
            break
        print("Please enter a name containing only letters and numbers.")

    # Get valid positive integer input for chips amount
    while True:
        try:
            player_balance = int(input("How many $ in chips would you like? "))
            if player_balance > 0:
                break
            print("Please enter a positive amount.")
        except ValueError:
            print("Please enter a valid number.")

    # Player setup
    player = Player(player_name, player_balance)

    while True:
        # Betting
        bet_amount = get_valid_bet_amount(player)
        player.bet(bet_amount)

        # Game initialization
        deck = Deck()
        dealer = Player("Dealer", 0)
        player.clear()
        dealer.clear()

        # Initial deal
        deal_cards(player, dealer, deck)
        print_initial_hands(player, dealer)

        # Player's turn
        player_busted = hit_or_stand(player, dealer, deck)

        # Dealer's turn if player hasn't busted
        if not player_busted:
            dealer.print_hand()
            dealer_busted = dealer_play(dealer, player, deck)
            determine_winner(player, dealer, bet_amount)

        # Display balance and play again
        player.print_balance()
        if input("Play again? [y]/n: ").lower() not in ['y', '']:
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
