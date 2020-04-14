from playingcard import playingCard
from random import *

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["d","c","h","s"]:
            for rank in range(1,14):
                self.cards.append(playingCard(suit,rank))
                
    def shuffle(self):
        """Randomize the order of the cards in the deck"""
        shuffle(self.cards)
        return self.cards

    def dealCard(self):
        """Remove the 1st card from the deck after shuffling"""
        return self.cards.pop(0)
    
    def cardLeft(self):
        """Return the number of cards remaining in the deck"""
        return str(len(self.cards))

def main(): #test
    deck = Deck()
    deck.shuffle()
    card = deck.dealCard()
    
    print(card)
    print(deck.cardLeft())

if __name__ == "__main__":
    main()
    
