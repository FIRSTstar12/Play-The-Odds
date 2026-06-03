from . import CardList

def points(playerList):
    sum = 0
    for card in playerList:
        valueKey = card.split(" of ")[0]
        if(valueKey != "Ace"):
            sum += CardList.values.get(valueKey)
        elif(valueKey == "Ace"):
            if(sum + 11 <= 21):
                sum += 11
            else:
                sum += 1
        else:
            return "something is broken"
    return sum