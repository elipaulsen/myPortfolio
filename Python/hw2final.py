# CS1210: HW2
######################################################################
# Complete the signed() function, certifying that:
#  1) the code below is entirely your own work, and
#  2) it has not been shared with anyone outside the intructional team.
#
def signed():
    return(["eplsn"])

######################################################################
# Import randint and shuffle from random module.
from random import randint, sample

######################################################################
# createDeck() produces a new, cannonically ordered, 52 card deck
# using a nested comprehension. Providing a value less than 13
# produces a smaller deck, like the semi-standard 40 card 4 suit 1-10
# deck used in many older card games (including tarot cards). Here,
# we'll use it with default values.
#
def createDeck(N=13, S=('spades', 'hearts', 'clubs', 'diamonds')):
    return([ (v, s) for s in S for v in range(1, N+1) ])



######################################################################
# Construct the representation of a given card using special unicode
# characters for hearts, diamonds, clubs, and spades. The input is a
# legal card, c, which is a (v, s) tuple. The output is a 2 or
# 3-character string 'vs' or 'vvs', where 's' here is the unicode
# character corresponding to the four standard suites (spades, hearts,
# diamonds or clubs -- provided), and v is a 1 or 2 digit string
# corresponding to the integers 2-10 and the special symbols 'A', 'K',
# 'Q', and 'J'.
#
# Example:
#    >>> displayCard((1, 'spades'))
#    'A♠'
#    >>> displayCard((12, 'hearts'))
#    'Q♡'
#
def displayCard(c):
    suits = {'spades':'\u2660', 'hearts':'\u2661', 'diamonds':'\u2662', 'clubs':'\u2663'}
    
    if c == []:
        return ''
    elif c[0] in range(2,11):
        return str(c[0]) + suits[c[1]]          #numbered card
        
    elif c[0] == 1:
        return 'A' + suits[c[1]]                #ace
        
    elif c[0] == 11:                            #jack
        return 'J' + suits[c[1]]
        
    elif c[0] == 12:                            #queen
         return 'Q' + suits[c[1]]
        
    elif c[0] == 13:                            #king
        return 'K' + suits[c[1]]
        



######################################################################
# Print out an indexed representation of the state of the table:
# foundation piles are numbered 0-3, corner piles 4-7.
#
# Example:
#   >>> showTable(F, C)
#     F0: 9♡...9♡
#     F1: 2♢...2♢
#     F2: 7♡...7♡
#     F3: 8♡...8♡
#     C4:
#     C5:
#     C6:
#     C7:
# Or, mid-game:
#     F0: 8♣...A♢
#     F1: J♣...J♣
#     F2: A♠...A♠
#     F3: 
#     C4: K♡...K♡
#     C5: 
#     C6: 
#     C7:
#
def showTable(F, C):
    for f in range(4):
        if len(F[f]) == 0:
            print('F{}:'.format(f))
        else:                               #first card in pile            last card in pile
            print('F{}: {}...{}'.format(f,displayCard(F[f][0]),displayCard(F[f][-1])))
            
    for c in range(4,8):
        if len(C[c-4]) == 0:
            print('C{}:'.format(c))
        else:                               #first card in pile            last card in pile
            print('C{}: {}...{}'.format(c,displayCard(C[c-4][0]),displayCard(C[c-4][-1])))
            
            
    

######################################################################
# Print out an indexed list of the cards in input list H, representing
# a hand. Entries are numbered starting at 8 (indexes 0-3 are reserved
# for foundation piles, and 4-7 are reserved for corners). The
# indexing is used to select cards for play.
#
# Example:
#   >>> showHand(H[0])
#   Hand: 8:A♢ 9:4♢ 10:3♡ 11:5♠ 12:6♠ 13:7♠ 14:8♠
#   >>> showHand(H[1])
#   Hand: 8:9♣ 9:5♢ 10:8♢ 11:9♢ 12:10♡ 13:A♠ 14:4♠
#
def showHand(H):
     hand = [displayCard(x) for x in H]
     print('Hand: ',end='')
     for x in range(len(H)):
         print(str(x+8)+':'+hand[x]+'  ',end='')
         
    
######################################################################
# We'll use deal(N, D) to set up the game. Given a deck (presumably
# produced by createDeck()), shuffle it, then deal 7 cards to each of
# N players, and seed the foundation piles with 4 additional cards.
# Returns D, H, F, where D is what remains of the deck, H is a list of
# N 7-card "hands", and F is a list of lists corresponding to the four
# "seeded" foundation piles.
# 
# Example:
#   >>> D, H, F = deal(2, D)
#   >>> len(D)
#   34
#   >>> len(H)
#   2
#   >>> H[0][:3]
#   [(5, 'clubs'), (12, 'clubs'), (3, 'diamonds')]
#   >>> F[2]
#   [(11, 'hearts')]
#
def deal(N,S):
    # Shuffle the deck, the return what's left of it after dealing 7
    # cards to each player and seeding the foundation piles.
    D = sample(S,len(S))            #shuffles deck
    H = []
    
    for player in range(N):
         H.append([])
         for i in range(7):
            H[player].append(D.pop(i))
            
    F = [[],[],[],[]]
    for c in range(len(F)):
        F[c].append(D.pop(c))
        
    return D,H,F







######################################################################
# Returns True if card c can be appended to stack S. To be legal, c
# must be one less in value than S[-1], and should be of the "other"
# color (red vs black).
#
# Hint: Remember, S might be empty, in which case the answer should
# not be True.
#
# Hint: Use the encapsulated altcolor(c1, c2) helper function to check
# for alternating colors.
#
# Example:
#   >>> legal((2, 'diamonds'), (1, 'spades'))
#   True
#   >>> legal((2, 'diamonds'), (1, 'hearts'))
#   False
#
def legal(S, c):
    
   
   
    def altcolor(c1, c2):
        if c1 == 'diamonds' or c1 == 'hearts':  #red
            if c2 == 'spades' or c2 == 'clubs': #black
                return True
            else:
                return False
        else:   #black
            if c2 == 'diamonds' or c2 == 'hearts':  #red
                return True
            else:
                return False
            
    
    if S[0] == c[0]+1 and altcolor(S[1], c[1]):
        return True
    else:
        return False




######################################################################
# Governs game play for N players (2 by default). This function sets
# up the game variables, D, H, F and C, then chooses the first player
# randomly from the N players. By convention, player 0 is the user,
# while all other player numbers are played by the auto player.
#
# Each turn, the current player draws a card from the deck D, if any
# remain, and then is free to make as many moves as he/she chooses. 
#
# Hint: fill out the remainder of the function, replacing the pass
# statements and respecting the comments.
# 

def play(N=2):
    # Set up the game.
    D, H, F = deal(N, createDeck())
    C = [[],[],[],[]]   # Corners, initially empty.

    # Randomly choose a player to start the game.
    player = randint(0, N-1)
    print('Player {} moves first.'.format(player))

    # Start the play loop; we'll need to exit explicitly when
    # termination conditions are realized.
    while True:
        # Draw a card if there are any left in the deck.
        H[player].append(D.pop(randint(0, len(D)-1)))

        print('\n\nPlayer {} ({} cards) to move.'.format(player, len(H[player])))
        print('Deck has {} cards left.'.format(len(D)))
        

        #Now show the table.
        showTable(F, C)
        
     

        # Let the current player have a go.
        if player != 0:
            automove(F, C, H[player])
        else:
            usermove(F, C, H[player])

        # Check to see if player is out; if so, end the game.
        if H[player] == []:
            print('\n\nPlayer {} wins!'.format(player))
            showTable(F, C)
            break

        # Otherwise, go on to next player.
        if player + 1 == N:
            player = 0
        else:
            player = player +1
######################################################################
# Prompts a user to play their hand.  See transcript for sample
# operation.
#
def usermove(F, C, hand):
    # valid() is an internal helper function that checks if the index
    # i indicates a valid F, C or hand index.  To be valid, it cannot
    # be an empty pile or an out-of-range hand index. Remember, 0-3
    # are foundation piles, 4-7 are corner piles, and 8 and up index
    # into the hand.
    def valid(i):
        if i in range(len(hand)): 
            return True
        else:
            return False

    # Ensure the hand is sorted, integrating newly drawn card.
    hand.sort()

    # Give some instruction.
    print('Enter your move as "src dst": press "/" to refresh display; "." when done with move')
    
    i = 0
    # Manage any number of moves.
    while i == 0:           # Until the user quits with a .
        # Display current hand.
        showHand(hand)

        # Read inputs and construct a tuple.
        move = []
        while not move or not valid(move[0]) or not valid(move[1]):
            move = input("Your move? ").split()
            
            if len(move) == 1:
                if move[0] == '.':
                    i = 1
                    break

                elif move[0] == '/':
                    print('\n')
                    showTable(F, C)
                    print('\n')
                    showHand(hand)
                    
            else:       

                try:
                    move = [int(move[0]), int(move[1])]
                    # Execute the command, which looks like [from, to].
                    # Remember, 0-3 are foundations, 4-7 are corners, 8+
                    # are from your hand.
                    #
                    # What follows here is an if/elif/else statement for
                    # each of the following cases.
        
                    # Playing a card from your hand to a foundation pile.
                    if move[1] < 4 and move[0] >= 8:
                        
                        if F[move[1]] == []:
                            print(('Moving {} to open foundation F{}').format(displayCard(hand[move[0]-8]),move[1]))
                            F[move[1]].append(hand.pop(move[0]-8))
                            
                        else:    
                            if legal(F[move[1]][-1],hand[move[0]-8]):   
                                print(('Moving {} onto F{}').format(displayCard(hand[move[0]-8]),move[1]))
                                F[move[1]].append(hand.pop(move[0]-8))
                            else:
                                print('illegal move')
        
        
        
                    # Moving a foundation pile to a foundation pile.
                    elif move[1] < 4 and move[0] < 4:
                        if legal(F[move[1]][-1],F[move[0]][0]):
                            F[move[1]].append(F[move[0]][-1])
                            print(('Moving F{} onto F{}').format(move[0],move[1]))
                            F[move[0]] = []
                        else:
                            print('illegal move')
                    
                    
                    
                    # Playing a card from your hand to a corner pile (K only to empty pile).
                    elif move[1] in range(4,8) and move[0] >= 8:
                        if C[move[1]-4] == []:
                            if hand[move[0]-8][0] == 13:
                                print(('Moving {} to open corner C{}').format(displayCard(hand[move[0]-8]),move[1]))
                                C[move[1]-4].append(hand.pop(move[0]-8))
                                
                            else:
                                print('only kings are allowed to be the first card in the corner')
                        else:
                            if legal(C[move[1]-4][-1],hand[move[0]-8]): 
                                print(('Moving {} onto C{}').format(displayCard(hand[move[0]-8]),move[1]))
                                C[move[1]-4].append(hand.pop(move[0]-8))
                            else:
                                print('illegal move')
                            
                            
                            
        
                    # Moving a foundation pile to a corner pile.;
                    elif move[1] in range(4,8) and move[0] < 4:
                        if C[move[1]-4] == []:
                        
                            if F[move[0]][0][0] == 13:
                                C[move[1]-4].append(F[move[0]][-1])
                                print(('Moving F{} to open corner C{}').format(move[0],move[1]))
                                F[move[0]] = []
                                
                            else:
                                print('only kings are allowed to be the first card in the corner')
                                
                        elif legal(C[move[1]-4][-1],F[move[0]][0]):
                            C[move[1]-4].append(F[move[0]][-1])
                            print(('Moving F{} onto C{}').format(move[0],move[1]))
                            F[move[0]] = []
                        else:
                            print('illegal move')
                        
                    else:
                        print('illegal move')
                        
                        
        
                except:
                    # Any failure to process ends up here.
                    print('Ill-formed move {}'.format(move))

            # If the hand is empty, return. Otherwise, reset move and
            # keep trying.
            if not hand:
                return
            move = []

######################################################################
# Plays a hand automatically using a fixed but not particularly
# brilliant strategy. The strategy involves consolidating the table
# (to collapse foundation and corner piles), then scanning cards in
# your hand from highest to lowest, trying to place each card. The
# process is repeated until no card can be placed. See transcript for
# an example.
#
def automove(F, C, hand):
    # Keep playing cards while you're able to move something.
    moved = True
    while moved:
        moved = False	# Change back to True if you move a card.

        # Start by consolidating the table.
        consolidate(F, C)

        # Sort the hand (destructively) so that you consider highest
        # value cards first.
        hand.sort()
        
        # Scan cards in hand from high to low value, which makes removing
        # elements easier.
        
        
        for i in range(len(hand)-1, -1, -1):
            
            
            
            # If current card is a king, place in an empty corner
            # location (guaranteed to be one).

            if hand[i][0] == 13:
                 # find which corner piles are empty
                for j in range(4):
                    if C[j] == []:
                        king = hand.pop(i)
                        
                        C[j].append(king)
                        moved = True
                        break   
                    
                print(('Moving {} to C{}').format(displayCard(king),j+4))
                
            else:    
                # Otherwise, try to place current card on an existing
                # corner or foundation pile.
                for j in range(4):
                    # Here, you have an if/elif/else that checks each of
                    # the stated conditions.
                    # Place current card on corner pile.
                    
                    if C[j]!=[] and legal(C[j][-1],hand[i]):
                        print(('Moving {} onto C{}').format(displayCard(hand[i]),j+4))
                        C[j].append(hand.pop(i))
                        moved = True
                        break
    
                    # Place current card on foundation pile.
                    elif F[j]!=[] and legal(F[j][-1],hand[i]):
                        print(('Moving {} onto F{}').format(displayCard(hand[i]),j))
                        F[j].append(hand.pop(i))
                        moved = True
                        break
                    
                    # Start a new foundation pile.
                    elif F[j] == []:
                        print(('Moving {} to open foundation F{}').format(displayCard(hand[i]),j))
                        F[j].append(hand.pop(i))
                        moved = True
                        break
       
              

######################################################################
# consolidate(F, C) looks for opportunities to consolidate by moving a
# foundation pile to a corner pile or onto another foundation pile. It
# is used by the auto player to consolidate elements on the table to
# make it more playable.
#
# Example:
#   >>> showTable(F, C)
#     F0: 6♢...6♢
#     F1: 10♣...10♣
#     F2: J♡...J♡
#     F3: Q♠...Q♠
#     C4: K♢...K♢
#     C5:
#     C6:
#     C7:
#   >>> consolidate(F, C)
#   >>> showTable(F, C)
#     F0: 6♢...6♢
#     F1:
#     F2: 
#     F3: 
#     C4: K♢...10♣
#     C5:
#     C6:
#     C7:
#
def consolidate(F, C):
    # Consider moving a foundation onto a foundation
    for i in range(4):
        for j in range(4):
            if i!=j and F[i] != [] and F[j] != [] and legal(F[j][-1],F[i][0]):
                F[j].append(F[i][-1])
                
                print(('Moving F{} onto F{}').format(i,j))
                F[i] = []
                
   
    # Consider moving a foundation onto a corner.
    for i in range(4):
        if F[i] != [] and F[i][0][0]==13:
            
            
            # find which corner piles are empty and append to the first open one
            for j in range(4):
                if C[j] == []:
                    C[j].append(F[i])
                    C[j] = C[j][0]
                    break   
                
            print(('Moving F{} to open corner C{}').format(i,j+4))
            F[i] = []
            
            
    for i in range(4):
        for j in range(4):
            if C[j] != [] and F[i] != [] and legal(C[j][-1],F[i][0]):
                C[j].append(F[i][-1])
                print(('Moving F{} onto C{}').format(i,j+4))
                F[i] = []
             
 


######################################################################
if __name__ == '__main__':
    # Play two-player version by default.
   play(2)


