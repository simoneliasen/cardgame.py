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
            new_player = Player(x, (input(f'Pick a suit Player {x}: ')), self.points)
            self.player_list.append(new_player)

    def print_players(self): 
        for x in self.player_list:
            print(x)

    def add_points(self):
        for x in self.player_list:
            if x.playersuit == card.cardsuit:
                x.points += 1
# BETA NOT DONE -- add extra card drawn
#    def subract_bonus(self):        
#        if all(self.points > 1 for x in self.player_list):
#            for x in self.player_list:
#                if x.playersuit == card.cardsuit:
#                    x.points -= 1

    def winner(self):
        for x in self.player_list:
            if x.points == 5:
                return f'Player{x.name} won!'

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

#Add points
PlayerManage.add_points()
#Print player objects
PlayerManage.print_players()
#Draws a card and show it
card = deck.drawCard()
card.show()

#Add points
PlayerManage.add_points()
#Print player objects
PlayerManage.print_players()
#Draws a card and show it
card = deck.drawCard()
card.show()

#Add points
PlayerManage.add_points()
#Print player objects
PlayerManage.print_players()
#Draws a card and show it
card = deck.drawCard()
card.show()

#Add points
PlayerManage.add_points()
#Print player objects
PlayerManage.print_players()
#Draws a card and show it
card = deck.drawCard()
card.show()

#Add points
PlayerManage.add_points()
#Print player objects
PlayerManage.print_players()
#Draws a card and show it
card = deck.drawCard()
card.show()

#Add points
PlayerManage.add_points()
#Print player objects
PlayerManage.print_players()
#Draws a card and show it
card = deck.drawCard()
card.show()

#Add points
PlayerManage.add_points()
#Print player objects
PlayerManage.print_players()
#Draws a card and show it
card = deck.drawCard()
card.show()

#Add points
PlayerManage.add_points()
#Print player objects
PlayerManage.print_players()
#Draws a card and show it
card = deck.drawCard()
card.show()

#Add points
PlayerManage.add_points()
#Print player objects
PlayerManage.print_players()
#Draws a card and show it
card = deck.drawCard()
card.show()

#Add points
PlayerManage.add_points()
#Print player objects
PlayerManage.print_players()
#Draws a card and show it
card = deck.drawCard()
card.show()

#Add points
PlayerManage.add_points()
#Print player objects
PlayerManage.print_players()
#Draws a card and show it
card = deck.drawCard()
card.show()

#Add points
PlayerManage.add_points()
#Print player objects
PlayerManage.print_players()
#Draws a card and show it
card = deck.drawCard()
card.show()

print(PlayerManage.winner())

#Functions to add:
#1. Pulle extra card if all points >= 1,2,3,4:
# Print only once (while loop?)
#2. Display message with points at last
#3. Integrate with flask

