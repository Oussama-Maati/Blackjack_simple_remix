from Deck import Deck
from Game import Game
from Player import Player

deck = Deck()

print("WELCOME TO BLACKJACK!\n")

name = input("Type the name of the player 1 :")
Player1 = Player(name)

name = input("Type the name of the player 2 :")
Player2 = Player(name)

game = Game(Player1, Player2, deck)

game.start()


while game.StateGame != "GameOver":
    game.play()



# GameOver = False
# while not GameOver:



