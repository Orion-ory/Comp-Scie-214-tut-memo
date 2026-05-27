import sys, random, stdio

def main():
    n = int(sys.argv[1]); 
    stdio.writeln("Running " + str(n) + " simulations.")
    nEvents = 0; 
    prnt = len(sys.argv) > 2
    sides = ["H","T"] # TODO: Remove this list, not yet done
    
    for i in range(n):
      # Simulate Alice
      if (prnt): stdio.write("Alice:")
      aliceLast = -1
      aliceCurrent = -1
      aliceTosses = 0

      while (not ((aliceLast == 0) and (aliceCurrent == 0))):
        aliceLast = aliceCurrent
        aliceCurrent = (int)(random.random() * 2); # 0 Head, 1 Tails
        aliceTosses += 1
        if (prnt): stdio.write(sides[aliceCurrent])

      # Simulate Bob
      if (prnt): stdio.write(" Bob:")
      bobLast = -1
      bobCurrent = -1
      bobTosses = 0

      while (not ((bobLast == 0) and (bobCurrent == 1))):
        bobLast = bobCurrent
        bobCurrent = (int)(random.random() * 2)
        bobTosses += 1
        if (prnt): stdio.write(sides[bobCurrent])

      if (aliceTosses < bobTosses):
         nEvents += 1
         if (prnt): stdio.write(" Alice has fewer.")

      if (prnt): stdio.writeln()
    
    prob = nEvents / n; 
    stdio.writeln(prob);    

if __name__ == '__main__': main()
