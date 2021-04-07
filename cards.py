import random  # put in the init for deck

"""
move represents type of move
    f = forward
    b = backward
    l = turn left
    r = turn right
    u = u-turn
"""

class Card:
    def __init__(self, priority, move, amount):
        self.priority = priority
        self.move = move
        self.amount = amount


    def __str__(self):
        return f"{self.move}, {self.amount}"

# **************** Test Code
    def applyCard(self, robotN):
        if self.move == 'f':
            robotN.moveFwd(self.amount)

        if self.move == 'b':
            pass

        if self.move == 'l':
            pass

# **************** Test Code


class Deck:
    def shuffleList(self):
        myDeck = []
        f = open('cards.txt', 'r')
        for line in f:
            line = line.replace('\n', '')
            priority, move, amount = line.split(', ')
            newCard = Card(priority, move, amount)
            myDeck.append(newCard)
        return myDeck


    def __init__(self):
        self.cardList = self.shuffleList()


    def printDeck(self):
        for card in self.cardList:
            print(card.priority, card.move, card.amount)

    def getCard(self):  # does it work?
        return self.cardList.pop()




if __name__ == "__main__":
    d = Deck()
    d.shuffleList()
    print(d.getCard())
