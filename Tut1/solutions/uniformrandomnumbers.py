import sys, random, stdio

def main():
    minVal = 1
    maxVal = 0
    total = 0
    n = 5
    for i in range(n):
        nxt = random.random()
        stdio.writeln(nxt)
        total += nxt
        minVal = min(minVal, nxt)
        maxVal = max(maxVal, nxt)
    stdio.writeln("Minimum: "+str(minVal))
    stdio.writeln("Maximum: "+str(maxVal))
    stdio.writeln("Average: "+str(total/n))

if __name__ == '__main__': main()
