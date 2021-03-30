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




d = Deck()
d.shuffleList()
d.printDeck()
