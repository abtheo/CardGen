#CardGen Genetic Algorithm
#Rule module
import cards

class Rule:
    #Sets the minimum required attributes
    def __init__(self):
        self.played = []
        self.effect = "Pickup 7 ya mug"

myDeck = cards.Deck()
blackjack = Rule()

blackjack.played = myDeck.getSelect(["jack", "ace"], ["hearts", "clubs"])
print(blackjack.played)
