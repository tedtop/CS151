

"""
This module defines the Card class, which represents a playing card.
"""

class Card:
    """
    Represents a playing card with a suit and rank.
    """
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
             'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

    def __init__(self, suit, rank):
        """
        Initialize a card with a suit and rank.

        Args:
            suit (str): The suit of the card (Hearts, Diamonds, Clubs, Spades)
            rank (str): The rank of the card (Ace, Two-Ten, Jack, Queen, King)
        """
        self.suit = suit
        self.rank = rank

    def get_value(self):
        """
        Returns the blackjack value of the card.
        Aces return 11 (the Player class will handle when it should be 1).
        Face cards return 10.
        Number cards return their numeric value.
        """
        if self.rank == 'Ace':
            return 11
        elif self.rank in ['King', 'Queen', 'Jack']:
            return 10
        else:
            # Convert written numbers to integers
            number_map = {
                'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5,
                'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10
            }
            return number_map[self.rank]

    def __str__(self):
        """Returns a string representation of the card (e.g., 'Ace of Spades')."""
        return f"{self.rank} of {self.suit}"


if __name__ == "__main__":
    # Test client for the Card class
    card = Card("Hearts", "Ace")
    print(card)
    print(card.get_value())
    card.set_value(1)
    print(card.get_value())