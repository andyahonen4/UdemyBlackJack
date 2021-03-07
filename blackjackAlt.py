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
    
class Player:
    
    def __init__(self,name):
        
        self.name = name
        self.chips = 50
                  
    #def draw(self):
              
    def __str__(self):
        return f"{self.name}, You currently have {self.chips} available chips."

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



play_again = True
# game runs until you have 0 chips
while play_again == True and user.chips > 0:

    #create and shuffle deck
    new_deck = Deck()
    new_deck.shuffle()
    
    #deal cards 
    user_hand = []
    user_total = 0
    user_aces = []
    
    user_card_one = new_deck.dealOne()
    user_card_two = new_deck.dealOne()
    
    d_hand = []
    d_total = 0
    d_aces = []
    
    d_card_one = new_deck.dealOne()
    d_card_two = new_deck.dealOne()
    
    
    #this makes a list for both hands
    user_hand.append(user_card_one)
    user_hand.append(user_card_two)
    
    d_hand.append(d_card_one)
    d_hand.append(d_card_two)
    
    #for every card in user's hand, add the value of the card to user's total hand value
    for card in user_hand:
        user_total += card.value

        # add Aces to a list. they can be used if user busts
        if card.rank == 'Ace':
            user_aces.append(card)

    #Ace card flexing logic:
    # if dealer's hit card brings them over 21, but the dealer has an ace that hasn't been flexed from 11 to 1...
    if user_total > 21 and len(user_aces) > 0:

        #ace gets flexed
        user_total -= 10

        #remove the ace from the list of Aces available to flex for user
        user_aces.pop()

    #same for dealer
    for card in d_hand:
        d_total += card.value

        if card.rank == 'Ace':
            d_aces.append(card)

        if d_total > 21 and len(d_aces) > 0:
            d_total -= 10
            d_aces.pop()
        
    
    # cards are dealt. user sees dealer's first card before betting
    print(f"\nDealer's first card....{d_hand[0]}. A total of {d_card_one.value}.\n")
     
    amount = int(input(f"Current chips: {user.chips}. What would you like to bet this round? "))
    
    
    # bet must be a non-zero & can't exceed their chip count
    while amount == 0 or amount > user.chips:
            print(f"You have {user.chips} total chips to bet. Choose another bet amount between 1 and {user.chips}: ")
    print(f"\nYour bet of {amount} has been placed.\n")
    
    
    #show their opening hand
    print(f"{user.name}, you've drawn....{user_hand[0]} and {user_hand[1]}. A total of {user_total}.\n")
    
    
    #if user doesn't have blackjack already, they can hit or stay
    while user_total < 21:
        user_move = input(f"You have {user_total}. Would you like to hit, or stay?(Type 'h' for hit or 's' for stay:) ")
        user_move = user_move.lower()

        if user_move == 's':
            #hand must be better than dealer's visible hand (only one dealer card shown so far)
            if user_total <= d_hand[0].value:
                print(f"You'll need to top the dealer's current hand of {d_hand[0].value}. Please select 'h' to do so.")
                continue
            break
        
        if user_move == 'h':
            hit_card = new_deck.dealOne()
            user_hand.append(hit_card)

            if hit_card.rank == 'Ace':
                user_aces.append(hit_card)
            
            user_total += hit_card.value

            while user_total > 21 and len(user_aces) > 0:
                user_total -= 10
                user_aces.pop()

            print(f"\n...{hit_card}. You now have {user_total}.")

    #dealer's turn (user has elected to stay with hand, or hasn't busted)       
    if user_total <= 21:

        #run dealer's turn function, and pass in the current values
        d_total = dealerTurn(user_total,d_hand,d_total,d_aces)
    
    #game over. outcomes:
    
    #user won
    if user_total <= 21:
        if user_total > d_total or d_total > 21:
            winnings = amount*2
            user.chips += winnings
            print(f"You've won the hand! You earned {winnings} chips, and you now have {user.chips} total chips.")
        
    #user lost           
    if d_total <= 21:
        if user_total < d_total:
            user.chips -= amount
            print(f"Dealer has won the hand! You've lost {amount} chips, and you now have {user.chips} total chips.")

        if user.chips == 0:
            print("You're all out of chips. Thanks for playing Blackjack!")
            play_again = False
            break

    #tie
    if user_total == d_total:
        user.chips += amount
        print(f"You've and the dealer tied, resulting in a push. You earned your {amount} chips back, and you now have {user.chips} total chips.")

    user_replay = input("Would you like to play again? y/n: ")
    if user_replay.lower() == "n":
        play_again = False
        break
    else:
        continue