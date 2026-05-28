import sys
import math
import stdio


def main():

    # The sides can be fractional, so float() them
    side1 = float(sys.argv[1])
    side2 = float(sys.argv[2])
    
    # We only want to use the result in our writeln() call,
    # so we can use it in-line (as opposed to saving it in
    # a separate variable called "diagonal" or similar)
    stdio.writeln(math.sqrt(side1*side1 + side2*side2))


if __name__ == '__main__':
    main()
