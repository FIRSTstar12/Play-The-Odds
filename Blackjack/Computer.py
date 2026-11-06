from . import PointValues
compulterCards = []
currentValue = 0

def getPoints():
    if(len(compulterCards) != 0):
        return PointValues.points(compulterCards)


def getShowCards():
    if(len(compulterCards) != 0):
        showCards = []
        for card in compulterCards:
            if(card != compulterCards[1]):
                showCards.append(card)
            else:
                showCards.append("Hidden Card")
        print("Computer Cards")
        for cards in showCards:
            print(cards)
    else:
        print("The computer has no cards")
def printCards():
    print("Computer Cards:")
    for card in compulterCards:
        print(card)
