
import random


class Card:

    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        # return f"{value} of {suit}"
        return "{} of {}".format(self.value, self.suit)


class Deck:

    def __init__(self):
        self.cards = [Card(suit, value)
                      for suit in Card.suits for value in Card.values]
        # for suit in Card.suits:
        #     for value in Card.values:
        #         self.cards.append(Card(suit, value))

    def __repr__(self):
        # return f"Deck of {self.count()} cards"
        return "Deck of {} cards".format(self.count())

    def _deal(self, number_cards):
        if self.count() == 0:
            raise ValueError("All cards have been dealt")
        number_to_deal = min(self.count(), number_cards)
        cards = self.cards[-number_to_deal:]
        self.cards = self.cards[:-number_to_deal]
        # returned_list = []
        # for counter in range(0, number_to_deal):
        #     returned_list.append(self.cards.pop())
        return cards

    def count(self):
        return len(self.cards)

    def deal_card(self):
        single_card_list = self._deal(1)
        return single_card_list[0]

    def deal_hand(self, number_cards):
        return self._deal(number_cards)

    def shuffle(self):
        if self.count() < len(Card.suits) * len(Card.values):
            raise ValueError("Only full decks can be shuffled")
        random.shuffle(self.cards)
        return self


if __name__ == "__main__":
    deck = Deck()
    print(deck)
    print(deck.count())
    print(deck.cards)
    deck.shuffle()
    print(deck.cards)
    print(deck.deal_hand(52))
    print(deck.deal_card())
