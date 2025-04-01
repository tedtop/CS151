# Ted Toporkov
# 12/06/2025
# player.py

"""
This module defines the Player class, which represents a player in the Blackjack game.
"""

class Player:
    """Represents a player in the Blackjack game."""
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.hand = []

    def print_hand(self, show_all=True):
        """
        Prints the player's hand.

        Args:
            show_all (bool): If False, only shows the first card and hides the rest
        """
        print("*************************")
        print(f"{self.name}'s hand:")
        print()
        if show_all:
            for card in self.hand:
                print(card)
            print()
            print(f"Hand value: {self.blackjack_hand_value()}")
        else:
            print(self.hand[0])  # Show first card
            print("*Face Down Card*")  # Hide second card
            print()
            print(f"Visible hand value: {self.hand[0].get_value()}")
        print("*************************")
        print()

    def print_first(self):
        """Prints only the first card in the player's hand."""
        print(f"{self.name}'s first card: {self.hand[0]}")

    def clear(self):
        """Clears the player's hand."""
        self.hand = []

    def deal_card(self, deck):
        """Adds a card to the player's hand from the given deck."""
        self.hand.append(deck.deal())

    def print_balance(self):
        """Prints the player's balance in a formatted way."""
        print(f"-----------------------------")
        print(f"{self.name}'s balance: ${self.balance}")
        print(f"-----------------------------")

    def get_balance(self):
        """Returns the player's balance."""
        return self.balance

    def bet(self, amount):
        """
        Subtracts the given amount from the player's balance if the balance is greater than or equal to the amount.
        Returns True if the bet was successful, False otherwise.
        """
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

    def win(self, amount):
        """Adds the given amount to the player's balance."""
        self.balance += amount

    def blackjack_hand_value(self):
        """Returns the value of the player's Blackjack hand."""
        value = 0
        aces = 0
        for card in self.hand:
            value += card.get_value()
            if card.rank == "Ace":
                aces += 1
        while value > 21 and aces > 0:
            value -= 10
            aces -= 1
        return value

    def blackjack(self):
        """Returns True if the player's hand is a Blackjack (two cards with a total of 21)."""
        return len(self.hand) == 2 and self.blackjack_hand_value() == 21