compulterCards = []
currentValue = 0

def getPoints():
    if(len(compulterCards) != 0):
        return compulterCards.points(compulterCards)


def getShowCards():
    if(len(compulterCards) != 0):
        for card in compulterCards:
            if(card != compulterCards[1]):
                compulterCards.append(card)
            else:
                continue
    else:
        print("The computer has no cards")
