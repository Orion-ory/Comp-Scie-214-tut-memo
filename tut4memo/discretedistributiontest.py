import stdio

from discretedistribution import discrete


def countValues(values):
    valueToCountMap = {val: 0 for val in set(values)}
    for val in values:
        valueToCountMap[val] += 1
    return valueToCountMap


def main():
    stdio.writeln("Testing discrete()...")
    stdio.writeln("Assert visually that the following ratios are roughly kept.")
    stdio.writeln("1.  a=[0.1, 0.2, 0.7], K=10000")
    values = discrete([0.1, 0.2, 0.7], 10000)
    stdio.writeln(countValues(values))
    stdio.writeln("2.  a=[0.1, 0.2, 0.3, 0.4], K=10000")
    values = discrete([0.1, 0.2, 0.3, 0.4], 10000)
    stdio.writeln(countValues(values))
    # add more tests here if you like :)


if __name__ == "__main__":
    main()