import random

from Card import Card


class Deck():
    def __init__(self):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
        self.cards = []
        for i,num in enumerate(self.deck):
            if i < 13:
                self.cards.append(Card(num,"Spades"))
            elif i < 26:
                self.cards.append(Card(num, "Clubs"))
            elif i < 39:
                self.cards.append(Card(num, "Hearts"))
            else:
                self.cards.append(Card(num, "Diamonds"))

    # For debug
    def printCards(self):
        for card in self.cards:
            print(card.num)

    def give_random(self):
        random_num = random.choice(range(len(self.cards)))
        random_card = self.cards[random_num]
        # self.cards.remove(random_num)
        del self.cards[random_num]
        return random_card

    def __len__(self):
        return self.cards.__len__()
