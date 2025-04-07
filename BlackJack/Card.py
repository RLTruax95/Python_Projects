#Class for creating individual cards
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.visibility = False