import random
import CardList

playerHiddenCard = random.choice(CardList.cards)
rankPH = playerHiddenCard.split(" of ")[0]
if(rankPH.isdigit()):
    valuePH = int(rankPH)
elif(rankPH == "King" or rankPH == "Queen" or rankPH == "Jack"):
    valuePH = 10
elif(rankPH == "Ace"):
    valuePH = 1
CardList.cards.remove(playerHiddenCard)
playerShownCard = random.choice(CardList.cards)
rankPS = playerShownCard.split(" of ")[0]
if(rankPS.isdigit()):
    valuePS = int(rankPS)
elif(rankPS == "King" or rankPS == "Queen" or rankPS == "Jack"):
    valuePS = 10
elif(rankPS == "Ace"):
    valuePS = 1
CardList.cards.remove(playerShownCard)

playerCardList.cards = [playerHiddenCard,playerShownCard]
if(valuePH == valuePS):
    valuePS = 11
    valuePH = 1

currentValue = valuePH + valuePS