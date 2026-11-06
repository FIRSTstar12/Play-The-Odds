from .CardList import remove,cards

userCards = input("Enter your current cards seperated by spaces (king ace 2 3...): ")
userCards = userCards.lower().split()
for card in userCards:
    remove(card)

while True:
    try:
        numPlayers = int(input("Enter the number of players beside yourself: "))
        break
    except ValueError:
        print("Please type a number.")

ops = []

for i in range(numPlayers):
    ops.append([])

print("There are: " + str(len(ops)) + " other players")

while True:
    turns = input("Please enter the turn order as follows(op1, me, op2...)")
    order = [name.strip().lower() for name in turns.split(",")]
    good = "me" in order
    for name in order:
        if name != "me":
            if not (name.startswith("op") and name[2:].isdigit() and 1 <= int(name[2:]) <= numPlayers):
                good = False
    if good:
        break
    print("Use 'me' and op1 to op" + str(numPlayers) + ", separated by commas.")

numTurns = 0
gameOver = False

while gameOver is not True:
    player = order[numTurns % len(order)]
    goAgain = False
    print("--- " + player + "'s turn ---")

    if player == "me":
        turnOver = False
        while turnOver is not True:
            currentRequest = ""
            whoIndex = -1

            # Best pick: someone asked for a card I also have
            for i in range(len(ops)):
                for card in ops[i]:
                    if card in userCards and currentRequest == "":
                        currentRequest = card
                        whoIndex = i

            # Next best: a card I have two or more of
            if currentRequest == "":
                for card in userCards:
                    if userCards.count(card) > 1:
                        currentRequest = card
                        break

            # Otherwise: the first card in my hand
            if currentRequest == "" and len(userCards) > 0:
                currentRequest = userCards[0]

            if currentRequest == "":
                newCard = input("You have no cards, so draw one. What card did you draw?: ").strip().lower()
                if newCard != "":
                    userCards.append(newCard)
                    remove(newCard)
                turnOver = True
            else:
                if whoIndex != -1:
                    print("I recomend asking op" + str(whoIndex + 1) + " if they have any " + str(currentRequest))
                else:
                    print("I recomend asking one of the players if they have any " + str(currentRequest))
                answer = input("What did they say?(y/n, or q to quit): ").strip().lower()
                if answer == "q":
                    gameOver = True
                    turnOver = True
                elif answer == "y":
                    while True:
                        try:
                            newCards = int(input("How many cards did you get?: "))
                            break
                        except ValueError:
                            print("Please type a number.")
                    for i in range(newCards):
                        userCards.append(currentRequest)
                        remove(currentRequest)
                    if whoIndex != -1:
                        ops[whoIndex] = [c for c in ops[whoIndex] if c != currentRequest]
                    # Got what you asked for, so you go again
                else:
                    turnOver = True
                    if whoIndex != -1:
                        ops[whoIndex] = [c for c in ops[whoIndex] if c != currentRequest]
                    newCard = input("What card did you draw? (press Enter if the pile is empty): ").strip().lower()
                    if newCard != "":
                        userCards.append(newCard)
                        remove(newCard)
            if len(cards) == 0:
                turnOver = True
    else:
        idx = int(player[2:]) - 1
        asked = input("What card did " + player + " ask for? (press Enter to skip): ").strip().lower()
        if asked != "":
            if asked not in ops[idx]:
                ops[idx].append(asked)
            target = input("Who did they ask? (me, op1, op2... or press Enter if unsure): ").strip().lower()
            if target == "me":
                if asked in userCards:
                    gave = input("Did you hand them over? (y/n): ").strip().lower()
                    if gave == "y":
                        userCards = [c for c in userCards if c != asked]
                        goAgain = True
            elif target.startswith("op") and target[2:].isdigit() and 1 <= int(target[2:]) <= numPlayers:
                got = input("Did they have any? (y/n): ").strip().lower()
                if got == "y":
                    tIdx = int(target[2:]) - 1
                    ops[tIdx] = [c for c in ops[tIdx] if c != asked]
                    goAgain = True

    if goAgain is not True:
        numTurns += 1
    if len(cards) == 0:
        gameOver = True

print("Game over!")