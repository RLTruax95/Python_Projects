from Deck import Deck
import os

class Gameplay:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = []
        self.player_score = 0
        self.dealer_hand = []
        self.dealer_score = 0
        self.game_active = True
#####################################################################
    def run_game(self):
        while self.game_active:
            self.deck.reset_deck()
            self.clear_table()
            self.starting_deal()
            # if self.check_for_blackjack(): continue
            self.player_command()
            self.check_scores()
            if self.player_score > 21: continue
            self.dealer_hand[1].visibilty = True
            self.dealer_command()
            self.check_scores()
            self.find_winner()
#####################################################################
#Handles the initial deal of 3 visible cards and 1 hidden
    def starting_deal(self):
        self.player_hand.append(self.deck.deal())
        self.player_hand[0].visibility = True
        self.dealer_hand.append(self.deck.deal())
        self.dealer_hand[0].visibility = True
        self.player_hand.append(self.deck.deal())
        self.player_hand[1].visibility = True
        self.dealer_hand.append(self.deck.deal())
#####################################################################
    def get_scores(self):
        self.player_score = 0
        self.dealer_score = 0
        for card in self.player_hand: self.player_score += card.value
        for card in self.dealer_hand: self.dealer_score += card.value
#####################################################################
    def check_scores(self):
        self.get_scores()
        if self.player_score > 21: print('Player Bust!')
        if self.dealer_score > 21: print('Dealer Bust!')
#####################################################################
    def check_for_blackjack(self):
        return True
#####################################################################
    def player_command(self):
        while True:
            self.display_cards()
            command = input("Enter your command (Hit or Stand): ")
            if command.lower() != "hit" and command.lower() != "stand": continue
            if command.lower() == "hit":
                self.player_hand.append(self.deck.deal())
                self.check_scores()
                if self.player_score > 21: return
            else:
                return
#####################################################################
    def display_cards(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Player:')
        for card in self.player_hand:
            print(f'{card.value} of {card.suit}')
        print('\nDealer')
        for card in self.dealer_hand:
            if card.visibility:
                print(f'{card.value} of {card.suit}')
            else:
                print('?? of ?????')
#####################################################################
    def dealer_command(self):
        while True:
            self.check_scores()
            if self.dealer_score < 16:
                self.dealer_hand.append(self.deck.deal())
                self.check_scores()
                if self.dealer_score > 21: return
            else:
                return
#####################################################################
    def clear_table(self):
        self.player_hand = []
        self.player_score = 0
        self.dealer_hand = []
        self.dealer_score = 0
#####################################################################
    def find_winner(self):
        if self.player_score > self.dealer_score:
            print('Player Wins!')
        elif self.player_score < self.dealer_score:
            print('Dealer Wins!')
        else:
            print('Push!')
#####################################################################
if __name__ == '__main__':
    game = Gameplay()
    game.run_game()