from Card import Card


class Player():
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.sum = 0
        self.is_stand = False

    def stand(self):
        print(f"{self.name} has chose to stand")
        self.is_stand = True

    def hit(self, card):
        print(f"{self.name} has chose to take a card")
        self.add_card(card)
        print(f"{self.name} : {self.sum}")

    def add_card(self, card):
        self.cards.append(card)
        if card.num == 10 or card.num == 11 or card.num == 12 or card.num == 13:
            self.sum += 10
        elif card.num == 14:
            if self.sum > 10:
                self.sum += 1
            else:
                self.sum += 11
        else:
            self.sum += card.num

    def reset_card(self):
        self.cards = []
        self.sum = 0