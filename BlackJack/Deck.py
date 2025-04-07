from Card import Card
import random

class Deck:
    def __init__(self):
        self.cards = []
        self.reset_deck()
#####################################################################
    def reset_deck(self):
        self.cards = []
        for suit in ['Spade', 'Club', 'Diamond', 'Heart']:
            for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
                self.cards.append(Card(suit, value))
#####################################################################
    def deal(self):
        return self.cards.pop(random.randint(0,len(self.cards)-1))