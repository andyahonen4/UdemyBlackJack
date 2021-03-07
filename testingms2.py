import random

#CARD
#SUIT, RANK, VALUE
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit



class Player:
    
    def __init__(self,name):
        
        self.name = name
        self.chips = 50

        def __str__(self):
            return f"{self.name}, You currently have {self.chips} available chips."

'''
Andy's bookmark
'''
    
class Deck:
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                #Create the Card Object
                created_card = Card(suit,rank)
                
                self.all_cards.append(created_card)
                
    def shuffle(self):
        
        random.shuffle(self.all_cards)
        
    def dealOne(self):
        return self.all_cards.pop()     

class Hand:
    def __init__(self):
        self.cards = []
        self.total = 0
        self.aces_to_flex = []

    def hitMe(self,hit_card):
        
        self.cards.append(hit_card)
        self.total += hit_card.value

        if hit_card.rank == 'Ace':
            self.aces_to_flex.append(hit_card)

        if self.total > 21 and len(self.aces_to_flex) > 0:
            self.total -= 10
            self.aces_to_flex.pop()
        return self.total

'''
# will run when user's turn is over, but only if user hasn't busted
def dealerTurn(user_total,d_hand,d_total,d_aces):
    if user_total == 21:
        print(f"{user_total}! You've got blackjack! The dealer must hit on 21 or else you win.")
    else:
        print(f"The dealer must match or beat your hand of {user_total} or else you win.")

    input(f"\nDealer has seen one card and sits at {d_card_one.value}. Enter any key to continue: ")
    
    print(f"\nDealer's second card is turned...{d_hand[1]}. Dealer has {d_total}.\n")
    
    #play until dealer matches or beats user hand
    while user_total > d_total:
        input("Dealer must draw again. Enter any key to continue: ")
        hit_card = new_deck.dealOne()
        d_hand.append(hit_card)

        #adds new card to dealer's hand'
        d_total += hit_card.value

        # see Ace card flexing logic in notes later below if dealer's hit card brings them over 21, but the dealer has an ace that hasn't been flexed from 11 to 1...
        if d_total > 21 and len(d_aces) > 0:
                
                d_total -= 10
                
                d_aces.pop()
            
        print(f"\nDealer's next card is...{hit_card}. Dealer now has {d_total}.\n")

    # pass on the new dealer total    
    return d_total

#game_on

name = input("Welcome to Blackjack! Please enter your name to start playing: ")
user = Player(name)

print(f"\nWelcome, {user.name}!\n")

print("You'll start the game with 50 chips.\n")


'''



play_again = True
# game runs until you have 0 chips
##while play_again == True and user.chips > 0:

#create and shuffle deck
new_deck = Deck()
new_deck.shuffle()

#deal cards 
#user_hand = []
u = Hand()
d = Hand()

u.hitMe(new_deck.dealOne())
u.hitMe(new_deck.dealOne())

for card in u.cards:
    print(card.value)

print(u.total,u.aces_to_flex,'\n')

u.hitMe(new_deck.dealOne())
u.hitMe(new_deck.dealOne())
u.hitMe(new_deck.dealOne())
u.hitMe(new_deck.dealOne())
u.hitMe(new_deck.dealOne())

for card in u.cards:
    print(card.value)

print(u.total,u.aces_to_flex,'\n')
'''
user.cards.append(new_deck.dealOne())
user.cards.append(new_deck.dealOne())
user.cards.append(new_deck.dealOne())
user.cards.append(new_deck.dealOne())
user.cards.append(new_deck.dealOne())
'''