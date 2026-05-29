import stdarray
import stdrandom
import stdio
import math
import sys


def main():
    num_hands = int(sys.argv[1])
    x = 0

    SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
    RANKS = [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
        "Ace",
    ]
    deck = []

    for i in range(52):
        deck += [i + 1]
    for i in range(52):
        r = stdrandom.uniformInt(i, 52)
        temp = deck[i]
        deck[i] = deck[r]
        deck[r] = temp
    # stdio.writeln(str(len(deck)))
    # for v in range len(deck):
    # stdio.writeln(str(deck[v]))

    for i in range(num_hands):
        stdio.writeln("")
        stdio.writeln("")
        for j in range(5):
            # p = stdrandom.uniformInt((5*(i) + j), 52)
            x = deck[5 * i + j]

            stdio.writef("%s of %s  \n", RANKS[(x % 13) - 1], SUITS[(x // 13) - 1])


if __name__ == "__main__":
    main()
