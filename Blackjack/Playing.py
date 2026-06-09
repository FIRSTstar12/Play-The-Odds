from . import Odds
from . import CardList
from . import User
from . import Computer
from . import Misc

def playing():
    done = False
    winner = ""

    print("Let's play some Blackjack!") #intro
    Misc.wait(3)
    print()
    print("Burning a card...") #burning a card
    Misc.wait(1.5)
    CardList.burn()

    print("Dealing cards...") #dealing cards
    Misc.wait(1.5)
    print()
    User.userCards.append(CardList.deal()) #user's first card is face up
    print()
    Misc.wait(1.5)
    Computer.compulterCards.append(CardList.deal()) #computer's first card is face up
    Misc.wait(1.5)
    User.userCards.append(CardList.deal()) #user's second card is face down
    Misc.wait(1.5)
    User.printCards() #shows the user their cards
    print()
    Misc.wait(1.5)
    Computer.compulterCards.append(CardList.deal()) #computer's second card is face down
    Misc.wait(1.5)
    print("Computer's visible cards:")
    print(Computer.getShowCards()) #shows the user the computer's face up card
    Misc.wait(5)

    #Player
    choose = ""
    while done == False:
        choose = input("Hit or Stay?: ")
        if choose == "Hit" or choose == "hit":
            User.userCards.append(CardList.deal())
            if User.getPoints() > 21:
                done = True
                winner = "Computer"
        elif choose == "Hint" or choose == "hint":
            print(Odds.oddsOfBust(User.getPoints()))
        else:
            done = True

    #Computer/Dealer
    while Computer.getPoints() <= 16:
        if Odds.oddsOfBust(Computer.getPoints()) <= 0.699:
            Computer.compulterCards.append(CardList.deal())
            if Computer.getPoints() > 21:
                winner = "User"
                break
        else:
            break

    if winner == "":
        if User.getPoints() > Computer.getPoints():
            winner = "User"
        elif User.getPoints() < Computer.getPoints():
            winner = "Computer"
        else:
            print("There was a tie, it's time for a draw off. You and the computer will draw, higher card will win")
            while User.getPoints() == Computer.getPoints():
                userCard = CardList.deal()
                User.userCards.append(userCard)
                compCard = CardList.deal()
                Computer.compulterCards.append(compCard)
                if User.getPoints() > Computer.getPoints():
                    winner = "User"
                elif User.getPoints() < Computer.getPoints():
                    winner = "Computer"
                else:
                    continue

    if winner == "User":
        print("You WIN!! :D")
    elif winner == "Computer":
        print("You lost :(")
    else:
        print("Tie? :|")
    User.printCards()
    Computer.getShowCards()