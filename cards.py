#Card / Deck module

allSuits = ['hearts', 'diamonds', 'spades', 'clubs']
allValues = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

class Deck:
    def __init__(self, cardList=None):
        if cardList:
            self.cards = cardList
        else:
            self.cards = [Card(value, suit) for value in allValues for suit in allSuits]

    def __repr__(self):
        temp = []
        for c in self.cards:
            temp.append(c.value + "-" + c.suit)
        return ', '.join(temp)

    #Returns list of all cards with properties
    def getter(self, properties):
        out = []
        for c in self.cards:
            for p in properties:
                if c.value == p or c.suit == p:
                    out.append(c)
                    break       
        return out
       
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return "{0}-{1}".format(self.value, self.suit)

