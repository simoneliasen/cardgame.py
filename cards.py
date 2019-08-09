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

    def show(self, card, player):
        for c in self.cards:
            c.show()

    def drawCard(self):
        return self.cards.pop()

# PLAYER OBJECT (instantiated via PlayerGroup)
class Player:
    def __init__(self, name, playersuit, points):
        self.name = name
        self.playersuit = playersuit
        self.points = points

    def __str__(self):
        return f'Player{self.name} Suit: {self.playersuit} Points: {self.points}'

#PLAYER MANAGEMENT
class PlayerGroup:
    def __init__(self):
        self.amount= []
        self.player_list = []
        self.points = 0
        self.subtracted1 = False
        self.subtracted2 = False
        self.subtracted3 = False
        self.subtracted4 = False

    def amount_of_players(self):
        self.amount = range(int(input("\nHow many players? ")))

    def create_players(self):
        for x in self.amount:
            new_player = Player(x, (input(f'Pick a suit Player {x}: ')), self.points)
            self.player_list.append(new_player)

    def print_players(self): 
        for player in self.player_list:
            print(player)

    def add_points(self):
        for x in self.player_list:
            if x.playersuit == card.cardsuit:
                x.points += 1

    def subtract_bonus1(self):
        if self.subtracted1:
            return
        if all(player.points >= 1 for player in self.player_list): 
            card = deck.drawCard() 
            print(f'Bonus card: {card.value} of {card.cardsuit}')
            for x in self.player_list:
                if x.playersuit == card.cardsuit:
                    x.points -= 1
            self.subtracted1 = True

    def subtract_bonus2(self):
        if self.subtracted2:
            return
        if all(player.points >= 2 for player in self.player_list): 
            card = deck.drawCard() 
            print(f'Bonus card: {card.value} of {card.cardsuit}')
            for x in self.player_list:
                if x.playersuit == card.cardsuit:
                    x.points -= 1
            self.subtracted2 = True

    def subtract_bonus3(self):
        if self.subtracted3:
            return
        if all(player.points >= 3 for player in self.player_list): 
            card = deck.drawCard() 
            print(f'Bonus card: {card.value} of {card.cardsuit}')
            for x in self.player_list:
                if x.playersuit == card.cardsuit:
                    x.points -= 1
            self.subtracted3 = True

    def subtract_bonus4(self):
        if self.subtracted4:
            return
        if all(player.points >= 4 for player in self.player_list): 
            card = deck.drawCard() 
            print(f'Bonus card: {card.value} of {card.cardsuit}')
            for x in self.player_list:
                if x.playersuit == card.cardsuit:
                    x.points -= 1
            self.subtracted4 = True

    def winner(self):
        for x in self.player_list:
            if x.points >= 5:
                return f'Player{x.name} won!'

    def initialize_round(self):
        print('\n')
        deck.shuffle()
        card.show()
        PlayerManage.add_points()
        PlayerManage.print_players()
        PlayerManage.subtract_bonus1()
        PlayerManage.subtract_bonus2()
        PlayerManage.subtract_bonus3()
        PlayerManage.subtract_bonus4()
        input("Press Enter to continue...")
   
# START GAME: Instantiate players + deck of cards
PlayerManage = PlayerGroup()
PlayerManage.amount_of_players()
PlayerManage.create_players()

#Create deck, and shuffle
deck = Deck()
deck.shuffle()

#draw cards until winner is found
while PlayerManage.winner() is None:
    card = deck.drawCard()
    PlayerManage.initialize_round()

#Print winner
print('\n')
print(PlayerManage.winner())