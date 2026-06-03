from . import PointValues
from . import Computer

userCards = []
shownCards = []
def getPoints():
    if(len(userCards) != 0):
        return PointValues.points(userCards)

def printCards():
    if(len(userCards) != 0):
        print("You have: ")
        for card in userCards:
            print(card)
    else:
        print("You have no cards")

def visable():
    print("You can see: ")
    printCards()
    Computer.getShowCards()

def getShowCards():
    if(len(userCards) != 0):
        for card in userCards:
            if(card != userCards[1]):
                shownCards.append(card)
            else:
                continue
    else:
        print("You have no cards")

