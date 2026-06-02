import random
import CardList
import User
import Computer

bustedP = False
stayP = False
winner = ""
newCard = ""
while(not stayP and not bustedP):

    choice = input("hit or stay?: ")
    if(choice == "hit"):
        newCard = random.choice(CardList.cards)
        User.playerCardList.append(newCard)
        rankN = newCard.split(" of ")[0]
        if(rankN.isdigit()):
            valueN = int(rankN)
        elif(rankN == "King" or rankN == "Queen" or rankN == "Jack"):
            valueN = 10
        elif(rankN == "Ace"):
            valueN = 1
        CardList.cards.remove(newCard)
        User.currentValue += valueN
        newCard = ""
        rankN = ""
        valueN = ""
        if(User.currentValue > 21):
            bustedP = True
            break
    elif(choice == "stay"):
        stayP = True
        break
    else:
        print("invalid input")

if(bustedP):
    winner = "Computer"