import random
"""Builds Classes necessary for a game of BlackJack"""

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_value(self):
        if self.rank in ['J','Q','K']:
            return 10
        elif self.rank == 'A':
            return 11
        else:
            return int(self.rank)

class Deck:
#Creates an individual Card for each suit,rank
    def __init__(self):
        self.cards = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.cards.append(card)

#Method to Shuffle the Deck
    def shuffle(self):
        random.shuffle(self.cards)

#Method to Deal each card
    def deal(self):
        return self.cards.pop()



#Creates a class that stores the Hand dealt
class Hand:
    def __init__(self):
        self.cards = []

#Adds a card to your hand
    def add_card(self, card):
        self.cards.append(card)

#Calculates the total in your hand
    def get_value(self):
        total = 0
        aces = 0

        for card in self.cards:
            total += card.get_value()
            if card.rank == 'A':
                aces += 1

        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        return total

