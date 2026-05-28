import sys, stdio, stdarray, random

def main():
    CARDS_PER_PLAYER = 13

    # number of players
    PLAYERS = 4
    
    NUMBER_OF_RUNS = int(sys.argv[1])

    suit = [ "Clubs", "Diamonds", "Hearts", "Spades" ]
    rank = [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace" ]
    handDescriptions = ["5-3-3-2", "4-4-3-2", "4-3-3-3"]

    # avoid hardwired constants
    SUITS = len(suit)
    RANKS = len(rank)
    CARDS = SUITS * RANKS

    if (CARDS_PER_PLAYER * PLAYERS > CARDS): raise Exception("Too many players")

    # initialize deck
    deck = stdarray.create2D(CARDS, 2, "")
    for i in range(RANKS):
        for j in range(SUITS):
            deck[SUITS*i + j][0] = rank[i]
            deck[SUITS*i + j][1] = suit[j]

    handCount = stdarray.create1D(3, 0)

    # Run the experiment NUMBER_OF_RUNS times
    for i in range(NUMBER_OF_RUNS):
        # shuffle (note we don't need a sorted deck to do this!)
        for j in range(CARDS):
            r = j + int(random.random() * (CARDS-j))
            t = deck[r]
            deck[r] = deck[j]
            deck[j] = t
        
        # Deal every card in the deck after shuffling, for this program each player receives 13 cards.
        # Note that the information of the hand is cleared after the players' hands are analysed.
        # Also note that since the deck is random we can give each player 13 cards instead of dealing in turn.
        hand = stdarray.create1D(4, 0)
        for j in range(PLAYERS * CARDS_PER_PLAYER):
            # Check the hand of the player for the distribution of suits.
            if(deck[j][1] == "Clubs"):
                hand[0]+=1
            elif(deck[j][1] == "Diamonds"):
                hand[1]+=1
            elif(deck[j][1] == "Hearts"):
                hand[2]+=1
            elif(deck[j][1] == "Spades"):
                hand[3]+=1
            else: raise Exception("Invalid suit!: "+deck[j][1])

            # If this is the last card dealt to the player.
            if (j % CARDS_PER_PLAYER == CARDS_PER_PLAYER - 1):
                hand = sorted(hand)  # sort trick (we do sorting later!)
                if(hand[0] == 2 and
                    hand[1] == 3 and
                    hand[2] == 3 and
                    hand[3] == 5):
                    handCount[0]+=1
                elif(hand[0] == 2 and
                    hand[1] == 3 and
                    hand[2] == 4 and
                    hand[3] == 4):
                    handCount[1]+=1
                elif(hand[0] == 3 and
                    hand[1] == 3 and
                    hand[2] == 3 and
                    hand[3] == 4):
                    handCount[2]+=1
                # Clear the hand/distribution record for the next players hand
                hand[0] = hand[1] = hand[2] = hand[3] = 0

    # Naive approach ignoring the possibility of draws
    bestHand = 0
    for i in range(1, len(handCount)):
        if (handCount[i] > handCount[bestHand]): bestHand = i

    numberOfHands = NUMBER_OF_RUNS * PLAYERS
    
    for i in range(len(handCount)):
        stdio.writeln("Probability of "+handDescriptions[i] + ": " + str(handCount[i] / numberOfHands))
    stdio.writeln(handDescriptions[bestHand] + " is the most likely.")

if __name__=='__main__': main()
