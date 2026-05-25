import random
import CardList

busted = False
stay = False
newCard = ""
while(not stay and not busted):
    choice = input("hit or stay?: ")
    if(choice == "hit"):
        newCard = random.choice(CardList.cards)
        rankN = newCard.split(" of ")[0]
        if(rankN.isdigit()):
            valueN = int(rankN)
        elif(rankN == "King" or rankN == "Queen" or rankN == "Jack"):
            valueN = 10
        elif(rankN == "Ace"):
            valueN = 1
        CardList.cards.remove(newCard)
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