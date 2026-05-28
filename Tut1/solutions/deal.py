#  Execution:    python3 deal.py NUM_PLAYERS
#
#  Deal 5-card hands at random to the given number of players.
#
#  $ python3 deal.py 3
#  4 of Spades
#  9 of Spades
#  Ace of Hearts
#  9 of Clubs
#  9 of Diamonds
#
#  6 of Spades
#  10 of Hearts
#  Queen of Hearts
#  8 of Hearts
#  King of Spades
#
#  7 of Hearts
#  8 of Diamonds
#  Queen of Spades
#  3 of Spades
#  4 of Diamonds
#
# Ported from Java version by Sedgewick and Wayne

import sys, random, stdarray, stdio

def main():

    CARDS_PER_PLAYER = 5

    # number of players
    PLAYERS = int(sys.argv[1])

    suit = [ "Clubs", "Diamonds", "Hearts", "Spades" ]
    rank = [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace" ]

    # avoid hardwired constants
    SUITS = len(suit)
    RANKS = len(rank)
    CARDS = SUITS * RANKS

    if (CARDS_PER_PLAYER * PLAYERS > CARDS): raise Exception("Too many players")

    # initialize deck
    deck = stdarray.create1D(CARDS,"")
    for i in range(RANKS):
        for j in range(SUITS):
            deck[SUITS*i + j] = str(rank[i]) + " of " + str(suit[j])

    # shuffle
    for i in range(CARDS):
        r = i + int(random.random() * (CARDS-i))
        t = deck[r]
        deck[r] = deck[i]
        deck[i] = t

    # print shuffled deck
    for i in range(PLAYERS * CARDS_PER_PLAYER):
        stdio.writeln(deck[i])
        if (i % CARDS_PER_PLAYER == CARDS_PER_PLAYER - 1): stdio.writeln()

if __name__=='__main__': main()
