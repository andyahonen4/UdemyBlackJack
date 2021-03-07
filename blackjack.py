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
            return f'{self.name}, You currently have {self.chips} available chips.'


    
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

#game_on

name = input("Welcome to Blackjack! Please enter your name to start playing: ")
user = Player(name)

print(f"\nWelcome, {user.name}!\n")

print("You'll start the game with 50 chips.\n")

play_again = True
# game runs until you have 0 chips
while play_again == True and user.chips > 0:

    #create and shuffle deck
    new_deck = Deck()
    new_deck.shuffle()
    
    #deal cards 
    u = Hand()
    d = Hand()

    u.hitMe(new_deck.dealOne())
    u.hitMe(new_deck.dealOne())
    
    d.hitMe(new_deck.dealOne())
    d.hitMe(new_deck.dealOne())

     # cards are dealt. user sees dealer's first card before betting
    print(f"\nDealer's first card....{d.cards[0]}. A total of {d.cards[0].value}.\n")
     
    amount = int(input(f"Current chips: {user.chips}. What would you like to bet this round? "))
    
    
    # bet must be a non-zero & can't exceed their chip count
    while amount == 0 or amount > user.chips:
            print(f"You have {user.chips} total chips to bet. Choose another bet amount between 1 and {user.chips}: ")
    print(f"\nYour bet of {amount} has been placed.\n")
    
    
    #show their opening hand
    print(f"{user.name}, you've drawn....{u.cards[0]} and {u.cards[1]}. A total of {u.total}.\n")
    
    
    #if user doesn't have blackjack already, they can hit or stay
    while u.total < 21:
        user_move = input(f"You have {u.total}. Would you like to hit, or stay?(Type 'h' for hit or 's' for stay:) ")
        user_move = user_move.lower()

        if user_move == 's':
            #hand must be better than dealer's visible hand (only one dealer card shown so far)
            if u.total <= d.cards[0].value:
                print(f"You'll need to top the dealer's current hand of {d.cards[0].value}. Please select 'h' to do so.")
                continue
            break
        
        if user_move == 'h':
            u.hitMe(new_deck.dealOne())

            print(f"\n...{u.cards[-1]}. You now have {u.total}.")

    #dealer's turn (user has elected to stay with hand, or hasn't busted)       
    if u.total <= 21:

        if u.total == 21:
            print(f"{u.total}! You've got blackjack! The dealer must hit on 21 or else you win.")
        else:
            print(f"The dealer must match or beat your hand of {u.total} or else you win.")

        input(f"\nDealer has seen one card and sits at {d.cards[0].value}. Enter any key to continue: ")
        
        print(f"\nDealer's second card is turned...{d.cards[1]}. Dealer has {d.total}.\n")
        
        #play until dealer matches or beats user hand
        while u.total > d.total:
            input("Dealer must draw again. Enter any key to continue: ")
            d.hitMe(new_deck.dealOne())
                
            print(f"\nDealer's next card is...{d.cards[-1]}. Dealer now has {d.total}.\n")

    #game over. outcomes:
    
    #user won
    if u.total <= 21:
        if u.total > d.total or d.total > 21:
            winnings = amount*2
            user.chips += winnings
            print(f"You've won the hand! You earned {winnings} chips, and you now have {user.chips} total chips.")
        
    #user lost           
    if d.total <= 21 or u.total > 21 or u.total < d.total:
        user.chips -= amount
        print(f"Dealer has won the hand! You've lost {amount} chips, and you now have {user.chips} total chips.")

        if user.chips == 0:
            print("You're all out of chips. Thanks for playing Blackjack!")
            play_again = False
            break

    #tie
    if u.total == d.total:
        user.chips += amount
        print(f"You've and the dealer tied, resulting in a push. You earned your {amount} chips back, and you now have {user.chips} total chips.")

    user_replay = input("Would you like to play again? y/n: ")
    if user_replay.lower() == "n":
        play_again = False
        break
    else:
        continue