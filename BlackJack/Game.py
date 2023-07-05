import Player
from Deck import Deck
from print_func import new_print_cards


class Game():
    def __init__(self, Player1, Player2, deck):
        self.player1 = Player1
        self.player2 = Player2
        self.deck = deck
        self.current_player = self.player1
        self.start_player = self.player1
        self.following_player = self.player2
        self.StateGame = ""

    def start(self):
        # print(len(self.deck))
        self.player1.add_card(self.deck.give_random())

        self.player2.add_card(self.deck.give_random())

        self.player1.add_card(self.deck.give_random())

        self.player2.add_card(self.deck.give_random())

        # print(self.player1.cards[0].num)
        # print(len(self.deck))
        print(f"{self.player1.name} has {self.player1.sum}")
        new_print_cards(self.player1.cards, False)

        print(f"{self.player2.name} has {self.player2.sum}")
        new_print_cards(self.player2.cards, False)

    def play(self):
        if not self.current_player.is_stand:
            action = input(f"So {self.current_player.name} Do you (h)it or (s)tand ?")
            while action != "h" and action != "s":
                action = input(f"So {self.current_player.name} Do you (h)it or (s)tand ?")

            if action == "h":
                self.current_player.hit(self.deck.give_random())
                print(f"{self.player1.name} has {self.player1.sum}")
                new_print_cards(self.player1.cards, False)

                print(f"{self.player2.name} has {self.player2.sum}")
                new_print_cards(self.player2.cards, False)
                self.check_after_hit()

            else:
                self.current_player.stand()

        if self.player1.is_stand and self.player2.is_stand:
            self.final_result()

        if self.current_player.name == self.player1.name:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def final_result(self):
        if self.player1.sum > self.player2.sum:
            print(f"The winner is {self.player1.name} with {self.player1.sum}")
            print(f"to {self.player2.sum} for {self.player2.name}")
        elif self.player2.sum > self.player1.sum:
            print(f"The winner is {self.player2.name} with {self.player2.sum}")
            print(f"to {self.player1.sum} for {self.player1.name}")
        else:
            print(f"It's a tie between {self.player1.name} and {self.player2.name} with a score of {self.player1.sum}")

        exit(0)

    def check_after_hit(self):
        if self.current_player.sum > 21:
            print(f"{self.current_player.name} is burned with {self.current_player.sum}")
            self.StateGame = "GameOver"

    def restart(self):
        action = input("Do you want to play again ? (y)es or (n)o")
        while action != "y" and action != "n":
            action = input("Do you want to play again ? (y)es or (n)o")

        if action == "y":
            self.deck = Deck()
            self.player1.reset_card()
            self.player2.reset_card()
            self.player1 = self.following_player
            self.player2 = self.start_player
            self.start_player = self.player1
            self.following_player = self.player2

        else:
            print("The game is finished !")
            exit(0)

    def print_board(self):
        print(f"{self.player1}")
