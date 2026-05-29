import random
import sys
import math
import stdrandom
import stdio


def main():
    num_sims = int(sys.argv[1])
    switch_wins = 0
    stay_wins = 0
    stay_success = 0
    switch_success = 0
    if len(sys.argv) > 2:
        stdio.writef("Running %d simulations", num_sims)

    i = 0
    for i in range(num_sims):

        Hdoor = random.choice([1, 4])
        Cdoor = random.choice([1, 4])
        Pdoor = random.choice([1, 4])

        while Hdoor == Pdoor and Hdoor == Cdoor:
            Hdoor = random.choice([1, 4])
    """  if len(sys.argv)> 2 : """

    if Cdoor == Pdoor:
        stay_wins += 1
    else:
        switch_wins += 1

    switch_success = switch_wins / num_sims
    stay_success = stay_wins / num_sims

    stdio.writeln(str(switch_success))
    stdio.writeln(str(stay_success))


if __name__ == "__main__":
    main()
