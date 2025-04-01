# Ted Toporkov
# 12/06/2025
# blackjack.py

"""
This is the main client file for the Blackjack game.
"""

from deck import Deck
from player import Player

def get_valid_bet_amount(player):
    """
    Prompts the user to enter a bet amount and validates that it is a positive integer
    and less than or equal to the player's current balance.

    Args:
        player (Player): The player object whose balance is checked against the bet amount.

    Returns:
        int: The valid bet amount entered by the user.
    """
    while True:
        try:
            bet_amount = int(input("How much $ would you like to bet? (specify number of dollars) "))
            if bet_amount > 0 and bet_amount <= player.get_balance():
                return bet_amount
            else:
                print("Invalid bet amount. Please enter a number between 1 and your current balance.\n")
        except ValueError:
            print("Invalid input. Please enter a number.")

def deal_cards(player, dealer, deck):
    """
    Deals the initial cards to the player and dealer.

    Args:
        player (Player): The player object.
        dealer (Player): The dealer object.
        deck (Deck): The deck of cards.
    """
    player.deal_card(deck)
    dealer.deal_card(deck)  # Dealer's first card face up
    player.deal_card(deck)
    dealer.deal_card(deck)  # Dealer's second card - we'll handle face down in print_hand

def print_initial_hands(player, dealer):
    """
    Prints the initial hands of the player and dealer, with the dealer's second card face down.

    Args:
        player (Player): The player object.
        dealer (Player): The dealer object.
    """
    print("Player's hand:")
    player.print_hand()
    print("\nDealer's hand:")
    dealer.print_hand(show_all=False)  # Show only the first card

def hit_until_stand(player, dealer, deck):
    """
    Handles the player's turn, where they hit until they stand or bust.

    Args:
        player (Player): The player object.
        dealer (Player): The dealer object.
        deck (Deck): The deck of cards.

    Returns:
        bool: True if the player busts, False otherwise.
    """
    while True:
        response = input("Hit? [y]/n: ").lower().strip() or 'y'
        if response != 'y':
            print("\nYou chose to stand.\n")
            return False
        print("\nYou chose to hit.\n")
        player.deal_card(deck)
        player.print_hand()
        dealer.print_hand(show_all=False)  # Only show dealer's first card

        player_value = player.blackjack_hand_value()
        if player_value > 21:
            print("You busted!")
            return True
        elif player_value == 21:
            print("21! Perfect score!")
            return False

def dealer_play(dealer, player, deck):
    """
    Handles the dealer's turn. Dealer must hit on 16 and below, stand on 17 and above.

    Args:
        dealer (Player): The dealer object.
        player (Player): The player object.
        deck (Deck): The deck of cards.

    Returns:
        bool: True if the dealer busts, False otherwise.
    """
    while dealer.blackjack_hand_value() < 17:
        print(f"Dealer must hit on {dealer.blackjack_hand_value()}.\n")
        dealer.deal_card(deck)
        dealer.print_hand()
        player.print_hand()
        if dealer.blackjack_hand_value() > 21:
            # print("Dealer busted!")
            return True
    print(f"Dealer must stand on {dealer.blackjack_hand_value()}.\n")
    return False

def determine_winner(player, dealer, bet_amount, player_busted, dealer_busted):
    """
    Determines the winner of the game and updates the player's balance accordingly.

    Args:
        player (Player): The player object.
        dealer (Player): The dealer object.
        bet_amount (int): The amount the player bet.
        player_busted (bool): True if the player busted, False otherwise.
        dealer_busted (bool): True if the dealer busted, False otherwise.
    """
    player_total = player.blackjack_hand_value()
    dealer_total = dealer.blackjack_hand_value()

    if player_busted:
        print("You busted!")
    elif dealer_busted:
        print("Dealer busted!")
        player.win(bet_amount * 2)
    elif player.blackjack():
        if dealer.blackjack():
            print("Push (tie).")
        else:
            print("Blackjack! You win 3:2.")
            player.win(int(bet_amount * 2.5))
    elif player_total == 21:
        print("21! You win 3:2.")
        player.win(int(bet_amount * 2.5))
    elif player_total > dealer_total:
        print("You win!")
        player.win(bet_amount * 2)
    elif player_total < dealer_total:
        print("Dealer wins.")
    else:
        print("Push (tie).")

def main():
    try:
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

        # Create player and print initial balance
        player = Player(player_name, player_balance)
        player.print_balance()

        # Game loop
        while True:
            # Get the player's bet amount and check if they have sufficient funds
            bet_amount = get_valid_bet_amount(player)
            if not player.bet(bet_amount):
                print("Insufficient funds.")
                continue

            # Print the game start message
            print()
            print("*****************")
            print("  GOOD LUCK !!!  ")
            print("*****************")
            print()

            # Create a new deck and the dealer
            deck = Deck()
            dealer = Player("Dealer", 0)

            # Clear the player and dealer's hands
            player.clear()
            dealer.clear()

            # Deal the initial cards
            deal_cards(player, dealer, deck)
            print_initial_hands(player, dealer)

            # Player's turn - hit until they stand or bust
            player_busted = hit_until_stand(player, dealer, deck)

            # If the player didn't bust, it's the dealer's turn
            if not player_busted:
                dealer.print_hand()
                dealer_busted = dealer_play(dealer, player, deck)
                determine_winner(player, dealer, bet_amount, player_busted, dealer_busted)

            # Print the player's updated balance
            player.print_balance()

            # Ask the player if they want to play again
            print("Would you like to play again? ([y]/n/q/quit)")
            response = input().lower()
            if response in ['n', 'q', 'quit']:
                print("\nThanks for playing! Come back soon!")
                break

    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing! Come back soon!")

if __name__ == "__main__":
    main()