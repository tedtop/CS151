

"""
This module defines the Deck class, which represents a deck of 52 playing cards.
"""

import random
from card import Card

class Deck:
    """Represents a deck of 52 playing cards."""
    def __init__(self):
        self.cards = []
        for suit in Card.suits:
            for rank in Card.ranks:
                self.cards.append(Card(suit, rank))
        random.shuffle(self.cards)

    def deal(self):
        """Returns and removes a card from the deck."""
        return self.cards.pop(0)

    def deck_size(self):
        """Returns the size of the deck."""
        return len(self.cards)

    def print_deck(self):
        """Prints all the cards in the deck."""
        for card in self.cards:
            print(card)


if __name__ == "__main__":
    # Test client for the Deck class
    deck = Deck()
    print(f"Deck size: {deck.deck_size()}")
    deck.print_deck()
    print(f"Dealt card: {deck.deal()}")
    print(f"Deck size: {deck.deck_size()}")