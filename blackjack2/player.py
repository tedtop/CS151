"""
Player module for Blackjack game.
Author: Ted Toporkov
Date: Dec 6, 2025
"""

class Player:
    """Represents a player in the Blackjack game."""
    def __init__(self, name, balance):
        """
        Initialize a player with a name and balance.

        Args:
            name (str): The player's name.
            balance (int): The player's initial chip balance.
        """
        self.name = name
        self.balance = balance
        self.hand = []

    def print_hand(self, show_all=True):
        """
        Prints the player's hand.

        Args:
            show_all (bool): If False, only shows the first card and hides the rest
        """
        print()
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
        """
        Adds a card to the player's hand from the given deck.

        Args:
            deck (Deck): The deck to draw a card from.
        """
        self.hand.append(deck.deal())

    def print_balance(self):
        """Prints the player's balance in a formatted way."""
        print(f"-----------------------------")
        print(f"{self.name}'s balance: ${self.balance}")
        print(f"-----------------------------")

    def get_balance(self):
        """
        Returns the player's current balance.

        Returns:
            int: The player's current balance.
        """
        return self.balance

    def bet(self, amount):
        """
        Subtracts the given amount from the player's balance if sufficient.

        Args:
            amount (int): The amount to bet.

        Returns:
            bool: True if bet is successful, False otherwise.
        """
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def win(self, amount):
        """
        Adds the given amount to the player's balance.

        Args:
            amount (int): The amount to add to the balance.
        """
        self.balance += amount

    def blackjack_hand_value(self):
        """
        Calculates the value of the player's Blackjack hand.

        Returns:
            int: The total value of the hand, with Aces counted optimally.
        """
        value = 0
        aces = 0
        for card in self.hand:
            value += card.get_value()
            if card.rank == "Ace":
                aces += 1

        # Adjust for Aces
        while value > 21 and aces > 0:
            value -= 10
            aces -= 1

        return value

    def blackjack(self):
        """
        Checks if the player has a Blackjack.

        Returns:
            bool: True if hand is a Blackjack (two cards totaling 21), False otherwise.
        """
        return len(self.hand) == 2 and self.blackjack_hand_value() == 21

if __name__ == "__main__":
    # Test client for the Player class
    from deck import Deck
    player = Player("Test Player", 1000)
    deck = Deck()

    # Deal two cards
    player.deal_card(deck)
    player.deal_card(deck)

    # Print hand and test methods
    player.print_hand()
    print(f"Hand value: {player.blackjack_hand_value()}")
    print(f"Is Blackjack: {player.blackjack()}")
