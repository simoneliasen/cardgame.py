import random

#CARD
class Card:
    def __init__(self, cardsuit, val):
        self.cardsuit = cardsuit
        self.value = val

    def show(self):
        print("{} of {}".format(self.value, self.cardsuit))

#DECK OF CARDS
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

#PLAYER MANAGEMENT
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

# BETA NOT DONE 
    def subtract_bonus1(self):
        if all(player.points >= 1 for player in self.player_list): #Works until here
                print('Cardbonus1')

    def subtract_bonus2(self):
        if all(player.points >= 2 for player in self.player_list): #Works until here
                print('Cardbonus2')

    def subtract_bonus3(self):
        if all(player.points >= 3 for player in self.player_list): #Works until here
                print('Cardbonus3')

    def subtract_bonus4(self):
        if all(player.points >= 4 for player in self.player_list): #Works until here
                print('Cardbonus4')

#EXAMPLE:
#Draw card if all >= 1
#If cardsuit = playersuits =- 1
#Don't run again if it returns true

#RANDOM SPAGHETTI BELOW
        # run_once = 0
        # while run_once == 0:
            # if all(player.points >= 1 for player in self.player_list): #Works until here
            #     print('Hello world')
                # run_once += 1
            # else:
            #     break


                # for x in self.player_list:
                #     if x.playersuit == card.cardsuit:
                #         x.points -= 1
                #         run_once += 1
                #         print('It worked')

    def winner(self):
        for x in self.player_list:
            if x.points == 5:
                return f'Player{x.name} won!'

# PLAYBER OBJECT (instantiated via PlayerGroup)
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

## A BOUNCH OF SPAGHETTI DOWNWARDS

#Add points
PlayerManage.add_points()
#Print player objects
PlayerManage.print_players()
#Draws a card and show it
card = deck.drawCard()
card.show()
#Subtract bonus check
PlayerManage.subtract_bonus1()

#Add points
PlayerManage.add_points()
#Print player objects
PlayerManage.print_players()
#Draws a card and show it
card = deck.drawCard()
card.show()
#Subtract bonus check
PlayerManage.subtract_bonus1()

#Add points
PlayerManage.add_points()
#Print player objects
PlayerManage.print_players()
#Draws a card and show it
card = deck.drawCard()
card.show()
#Subtract bonus check
PlayerManage.subtract_bonus1()

#Add points
PlayerManage.add_points()
#Print player objects
PlayerManage.print_players()
#Draws a card and show it
card = deck.drawCard()
card.show()
#Subtract bonus check
PlayerManage.subtract_bonus1()

#Add points
PlayerManage.add_points()
#Print player objects
PlayerManage.print_players()
#Draws a card and show it
card = deck.drawCard()
card.show()
#Subtract bonus check
PlayerManage.subtract_bonus1()

#Add points
PlayerManage.add_points()
#Print player objects
PlayerManage.print_players()
#Draws a card and show it
card = deck.drawCard()
card.show()
#Subtract bonus check
PlayerManage.subtract_bonus1()

#Print winner
print(PlayerManage.winner())

