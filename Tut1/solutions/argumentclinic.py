import sys
import stdio


def main():
    if len(sys.argv) == 1:
        stdio.writeln("*crickets*")
    if len(sys.argv) == 2:
        stdio.writeln(sys.argv[1] + " is arguing with themself.")
    if len(sys.argv) == 3:
        stdio.writeln(sys.argv[1] + " is having an argument with " + sys.argv[2] + ".")
    if len(sys.argv) > 3:
        stdio.writeln("Much hilarity ensues.")


if __name__ == '__main__':
    main()
