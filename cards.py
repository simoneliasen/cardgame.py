import random

#Card
class Card:
    def __init__(self, cardsuit, val):
        self.cardsuit = cardsuit
        self.value = val

    def show(self):
        print("{} of {}".format(self.value, self.cardsuit))

#Deck of cards
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

    def show(self, card, player): #in code (keep)
        for c in self.cards:
            c.show()

    def drawCard(self):
        return self.cards.pop()

#Player Management
class PlayerGroup:
    def __init__(self):
        self.amount= []
        self.player_list = []
        self.points = 0

    def amount_of_players(self):
        self.amount = range(int(input("How many players? ")))

    def create_players(self):
        for x in self.amount:
            new_player = Player(x, (input("Pick a suit: ")), self.points)
            self.player_list.append(new_player)

    def print_players(self): 
        for x in self.player_list:
            print(str(x))

# Player Object (instatiated in PlayerGroup)
class Player:
    def __init__(self, name, playersuit, points):
        self.name = name
        self.playersuit = playersuit
        self.points = points

    def __str__(self):
        return f'Player{self.name} Suit: {self.playersuit} Points: {self.points}'


# Instantiate PlayerGroup + and print list containing instatiated players
PlayerManage = PlayerGroup()
PlayerManage.amount_of_players()
PlayerManage.create_players()

#Create deck, and shuffle
deck = Deck()
deck.shuffle()

#Draws a card and show it
card = deck.drawCard()
card.show()

#If drawn cards is = player suit ( player point + +)
print(card.cardsuit) #suit of drawn card

#Print player objects
PlayerManage.print_players()
