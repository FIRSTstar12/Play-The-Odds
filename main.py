import random

cards = [
    "Ace of Hearts", "2 of Hearts", "3 of Hearts", "4 of Hearts",
    "5 of Hearts", "6 of Hearts", "7 of Hearts", "8 of Hearts",
    "9 of Hearts", "10 of Hearts", "Jack of Hearts",
    "Queen of Hearts", "King of Hearts",

    "Ace of Diamonds", "2 of Diamonds", "3 of Diamonds", "4 of Diamonds",
    "5 of Diamonds", "6 of Diamonds", "7 of Diamonds", "8 of Diamonds",
    "9 of Diamonds", "10 of Diamonds", "Jack of Diamonds",
    "Queen of Diamonds", "King of Diamonds",

    "Ace of Clubs", "2 of Clubs", "3 of Clubs", "4 of Clubs",
    "5 of Clubs", "6 of Clubs", "7 of Clubs", "8 of Clubs",
    "9 of Clubs", "10 of Clubs", "Jack of Clubs",
    "Queen of Clubs", "King of Clubs",

    "Ace of Spades", "2 of Spades", "3 of Spades", "4 of Spades",
    "5 of Spades", "6 of Spades", "7 of Spades", "8 of Spades",
    "9 of Spades", "10 of Spades", "Jack of Spades",
    "Queen of Spades", "King of Spades"
]

playerHiddenCard = random.choice(cards)
rankPH = playerHiddenCard.split(" of ")[0]
if(rankPH.isdigit()):
    valuePH = int(rankPH)
elif(rankPH == "King" or rankPH == "Queen" or rankPH == "Jack"):
    valuePH = 10
elif(rankPH == "Ace"):
    valuePH = 1
cards.remove(playerHiddenCard)
playerShownCard = random.choice(cards)
rankPS = playerShownCard.split(" of ")[0]
if(rankPS.isdigit()):
    valuePS = int(rankPS)
elif(rankPS == "King" or rankPS == "Queen" or rankPS == "Jack"):
    valuePS = 10
elif(rankPS == "Ace"):
    valuePS = 1
cards.remove(playerShownCard)

playerCards = [playerHiddenCard,playerShownCard]
if(valuePH == valuePS):
    valuePS = 11
    valuePH = 1

currentValue = valuePH + valuePS

compHiddenCard = random.choice(cards)
rankCH = compHiddenCard.split(" of ")[0]
if(rankCH.isdigit()):
    valueCH = int(rankCH)
elif(rankCH == "King" or rankCH == "Queen" or rankCH == "Jack"):
    valueCH = 10
elif(rankCH == "Ace"):
    valueCH = 1
cards.remove(compHiddenCard)
compShownCard = random.choice(cards)
rankCS = compShownCard.split(" of ")[0]
if(rankCS.isdigit()):
    valueCS = int(rankCS)
elif(rankCS == "King" or rankCS == "Queen" or rankCS == "Jack"):
    valueCS = 10
elif(rankCS == "Ace"):
    valueCS = 1
cards.remove(compShownCard)

compCards = [compHiddenCard,compShownCard]
if(valueCH == valueCS):
    valueCS = 11
    valueCH = 1

busted = False
stay = False
newCard = ""
while(not stay and not busted):
    choice = input("hit or stay?: ")
    if(choice == "hit"):
        newCard = random.choice(cards)
        rankN = newCard.split(" of ")[0]
        if(rankN.isdigit()):
            valueN = int(rankN)
        elif(rankN == "King" or rankN == "Queen" or rankN == "Jack"):
            valueN = 10
        elif(rankN == "Ace"):
            valueN = 1
        cards.remove(newCard)
        currentValue += valueN
        newCard = ""
        rankN = ""
        valueN = ""
        if(currentValue > 21):
            busted = True
            break
    elif(choice == "stay"):
        stay = True
        break
    else:
        print("invalid input")