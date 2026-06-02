import Odds
import CardList
import User
import Computer

busted = False
stay = False
winner = ""

CardList.burn()

User.userCards.append(CardList.deal()) 
Computer.compulterCards.append(CardList.deal())
User.userCards.append(CardList.deal())
User.printCards()
Computer.compulterCards.append(CardList.deal())
print(Computer.getShowCards())

#Player
choose = ""
while not busted or not stay:
    choose = input("Hit or Stay?: ")
    if choose == "Hit" or choose == "hit":
        User.userCards.append(CardList.deal())
        if User.getPoints() > 21:
            busted = True
            winner = "Computer"
    elif choose == "Hint" or choose == "hint":
        print(Odds.oddsOfBust(User.getPoints()))
    else:
        stay = True

#Computer/Dealer
while Computer.getPoints() < 21:
    if Odds.oddsOfBust(User.getPoints()) <= 69.9:
        Computer.compulterCards.append(CardList.deal())
        if Computer.getPoints() < 21:
            winner = "User"
            break
    else:
        break

if User.getPoints() > Computer.getPoints():
    winner = "User"
elif User.getPoints() < Computer.getPoints():
    winner = "Computer"
else:
    print("There was a tie, it's time for a draw off. You and the computer will draw, higher card will win")
    