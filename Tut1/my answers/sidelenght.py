import sys
import math
import stdio


def main():
    x = 0.0
    y = 0.0

    a = len(sys.argv)
    if a < 3:
        stdio.writeln("  please insert 2 floating point coords")
    else:
        x = float(sys.argv[1])
        y = float(sys.argv[2])
        q = x**2 + y**2
        dis = math.sqrt(q)
        stdio.writeln(str(dis))


if __name__ == "__main__":
    main()
