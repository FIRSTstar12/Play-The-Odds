import Blackjack
import Blackjack.CardList
import Blackjack.Computer
import Blackjack.Odds
import Blackjack.PointValues
import Blackjack.User
import Blackjack.Playing
import GoFishCounter
# import GoFishCounter.CardList
import GoFishCounter.Playing

game = input("Do you want to play Blackjack or win Go Fish? (b/g)")
if "b" in game.lower():
    Blackjack.Playing.playing()
else:
    # GoFishCounter.Playing.play_game()
    print()