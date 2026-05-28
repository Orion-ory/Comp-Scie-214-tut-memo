import random
import sys
import stdio
import math


def main():
    numb_sims = int(sys.argv[1])
    stay_win = 0
    switch_win = 0

    for i in range(numb_sims):

        door1 = random.choice([0, 1])
        door2 = random.choice([0, 1])
        door3 = random.choice([0, 1])
        doors = [door1, door2, door3]
        stay_choice = random.choice(doors)
        switch_choice = random.choice(doors)

        new_door = doors[random.randrange(1, 3)]
        while id(new_door) == id(switch_choice):
            new_door = doors[random.randrange(1, 3)]

        switch_choice = new_door

        stay_win += stay_choice
        switch_choice += switch_choice

    stay_success = stay_win / numb_sims
    switch_success = switch_win / numb_sims

    stdio.writeln(str(stay_success))
    stdio.writeln(str(switch_success))
   


if __name__ == "__main__":
    main()
