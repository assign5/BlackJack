class playingCard:

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def value(self):
        if self.rank == "ace":
            return 1
        elif self.rank == "jack" or self.rank == "queen" or self.rank == "king":
            return 10
        else:
            return int(self.rank)
    def __str__(self):
        return ('{0} of {1}'.format(self.rank, self.suit))


    
def main():
    card1 = playingCard("ace","jack")
    #print(card1.getRank())
    print(card1.__str__())
    
if __name__ == "__main__":
    main()

