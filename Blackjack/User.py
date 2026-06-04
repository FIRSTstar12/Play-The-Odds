from . import PointValues
from . import Computer

userCards = []
def getPoints():
    if len(userCards) != 0:
        return PointValues.points(userCards)
    return 0

def printCards():
    if len(userCards) != 0:
        print("You have:")
        for card in userCards:
            print(card)
    else:
        print("You have no cards")

def visable():
    print("You can see: ")
    printCards()
    print(Computer.getShowCards())

def getShowCards():
    if(len(userCards) != 0):
        shownCards = []
        for card in userCards:
            if(card != userCards[1]):
                shownCards.append(card)
            else:
                continue
    else:
        print("You have no cards")
        return []
    return shownCards

