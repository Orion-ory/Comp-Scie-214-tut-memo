import sys
import random
import stdrandom
import stdio
import math


def main():

    num_sims = int(sys.argv[1])
    alicefirst = 0
    probability = 0.0
    i = 0

    for i in range(num_sims):
        A_prev = "A"
        A_cur = "B"
        B_prev = "C"
        B_cur = "D"
        A_win = False
        B_win = False

        while A_win != True and B_win != True:

            if not A_win:
                A_prev = A_cur
                A_cur = random.choice(["H", "T"])
            if not B_win:
                B_prev = B_cur
                B_cur = random.choice(["H", "T"])

            if B_prev == "H" and B_cur == "T":
                B_win = True
            if A_cur == A_prev and A_cur == "H":
                if B_win == False and A_win == False:
                    alicefirst += 1
                    A_win = True
                else:
                    A_win = True
        A_cur = "A"
        A_prev = "B"
        B_cur = "C"
        B_prev = "D"
        A_win = False
        B_win = False

    probability = alicefirst / num_sims
    stdio.writeln(str(probability))


if __name__ == "__main__":
    main()
