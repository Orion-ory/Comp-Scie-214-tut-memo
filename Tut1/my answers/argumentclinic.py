import sys
import stdio


def main():
    num = len(sys.argv)
    if num == 1:
        stdio.writeln("*crickets*")
    if num == 2:
        stdio.writef(" %s is arguing with themselves.", sys.argv[1])
    if num == 3:
        stdio.writef("%s is having an argument with %s.", sys.argv[1], sys.argv[2])
    if num == 4:
        stdio.writeln("Much hilarity ensues.")
    if num == 5:
        stdio.writeln("Much hilarity ensues.")


if __name__ == "__main__":
    main()
