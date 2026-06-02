import User
import Computer
import CardList
import PointValues

def optimalCard(currentPointVal):
    optimized = {}
    for card in CardList.cards:
        valueKey = card.split(" of ")[0]
        if valueKey == "Ace":
            if currentPointVal + 11 <= 21:
                cardValue = 11  
            else:
                cardValue = 1
        else:
            cardValue = CardList.values[valueKey]

        deckTotal = currentPointVal + cardValue

        if deckTotal == 21:
            optimized[card] = 0
        elif deckTotal > 21:
            optimized[card] = 5
        else:
            optimized[card] = min(21 - deckTotal, 5)

    return optimized

def numOfOptimalCards(currentPointVal):
    num5 = 0
    not5 = 0
    optimal = optimalCard(currentPointVal)
    for key,value in optimal.items():
        if value == 5:
            num5 += 1
        else:
            not5 += 1
    return not5

def oddsOfBust(currentPointVal):
    total = len(CardList.cards)
    safeCards = numOfOptimalCards(currentPointVal)
    bustCards = total - safeCards

    return bustCards / total