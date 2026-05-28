import sys
import random
import stdio


def main():
    x = []
    i = 0
    for i in range(5):
        x += [random.random()]
        stdio.writef("%.14f \n", x[i])

    stdio.writef(
        "Minimum: %.14f \nMaximum: %.14f \nAverage: %.14f \n",
        min(x),
        max(x),
        sum(x) / len(x),
    )


if __name__ == "__main__":
    main()
