import User
import Computer
import CardList
def ace():
    if User.currentValue + 11 > 21:
        User.currentValue += 1
    else:
        User.currentValue += 11

def points(user):
    if user == "user":
        player = User
    else:
        player = Computer

    CardList.values.get(CardList.cards.index(player))