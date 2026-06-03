from . import PointValues
compulterCards = []
showCards = []
currentValue = 0

def getPoints():
    if(len(compulterCards) != 0):
        return PointValues.points(compulterCards)


def getShowCards():
    if(len(compulterCards) != 0):
        for card in compulterCards:
            if(card != compulterCards[1]):
                showCards.append(card)
            else:
                continue
        return showCards
    else:
        print("The computer has no cards")
