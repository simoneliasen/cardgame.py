import random

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print("{} of {}".format(self.value, self.suit))

    def drawCard(self):
        return self.cards.pop()


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def show(self):
        for c in self.cards:
            c.show()

    def drawCard(self):
        return self.cards.pop()



class PlayerGroup:
    def __init__(self):
        self.suits= []

    def player_dict(self):
        player_dict = {}
        keys = range(int(input("How many players? ")))
        values = self.suits
        for i in keys:
            self.suits.append(input("Pick a suit: "))
            player_dict[i] = values[i]
        print(player_dict)

class PointSystem:
    pass



class Player:
    def __init__(self, points, suit):
        self.suit = suit
        self.points = points


# Instantiate PlayerGroup + print player_dict
players = PlayerGroup()
players.player_dict()

#Create deck, and shuffle
deck = Deck()
deck.shuffle()

#Draws a card and show it
card = deck.drawCard()
card.show()

# If card is equal to player_suit: +1 point

#Draw a new card

#if all players has above 1 point, draw minus card

#if suit == minus card: minus 1 point

#Make minus card only able to run once, every "milestone"


#When one player gets 5 points, the player wins



        # for i in range (int(input("How many players? "))):
        #     self.suit = input("Pick a suit: ")
    #
    # def amount(self):
    #     for i in range(int(input("How many players? "))):
    #         self.player_number.append(i)

    # def playersuits(self):
    #     for i in self.player_number:
    #         self.suit = input("Pick a suit: ")

    # def printplayers(self):
    #     for i in self.player_number:
    #         print(i)
