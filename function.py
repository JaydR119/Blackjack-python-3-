#All functions for Blackjack game are written here

#Function to simulate taking a bet
def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('\nHow many chips would you like to bet? '))
        except ValueError:
            print('\nSorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("\nSorry, your bet can't exceed",chips.total)
            else:
                break

#Fuction to take a hit
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

#Function to hit or stand
def hit_or_stand(deck,hand):
    global playing
    
    while True:
        x = input("\nWould you like to Hit or Stand? Enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("\nPlayer stands. Dealer is playing.")
            playing = False

        else:
            print("\nSorry, please try again.")
            continue
        break

#Function to show some cards & all cards
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

#Function for end-game scenarios
def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")
