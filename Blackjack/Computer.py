import random
import CardList

compHiddenCard = random.choice(CardList.cards)
rankCH = compHiddenCard.split(" of ")[0]
if(rankCH.isdigit()):
    valueCH = int(rankCH)
elif(rankCH == "King" or rankCH == "Queen" or rankCH == "Jack"):
    valueCH = 10
elif(rankCH == "Ace"):
    valueCH = 1
CardList.cards.remove(compHiddenCard)
compShownCard = random.choice(CardList.cards)
rankCS = compShownCard.split(" of ")[0]
if(rankCS.isdigit()):
    valueCS = int(rankCS)
elif(rankCS == "King" or rankCS == "Queen" or rankCS == "Jack"):
    valueCS = 10
elif(rankCS == "Ace"):
    valueCS = 1
CardList.cards.remove(compShownCard)

compCardList.cards = [compHiddenCard,compShownCard]
if(valueCH == valueCS):
    valueCS = 11
    valueCH = 1