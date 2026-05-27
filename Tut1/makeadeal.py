import sys, random, stdio

def main():
    # Note for this question that you could make this solution code more elegant by noting
    # that either the first or second choice of door is the
    # winning door, so you only actually need to estimate the probability P of one of these
    # strategies winning.  Then the estimate of the probability the other strategy winning
    # is simply 1-P.

    n = int(sys.argv[1]); 
    stdio.writeln("Running " + str(n) + " simulations.")
    nStayWins = 0
    nChangeWins = 0
    prnt = len(sys.argv) > 2
    for i in range(n):
      winningDoor = int(random.random() * 3)
      firstChoice = int(random.random() * 3)
      openedDoor = -1

      # Choose a door to open that is not the winning door, and not the first choice.
      while ((openedDoor == -1) 
             or (winningDoor == openedDoor)
             or (firstChoice == openedDoor)):
        openedDoor = int(random.random() * 3)

      secondChoice = -1; # illegal door for debugging
      # Second choice will be the unopened door that is not the first choice
      for j in range(3):
        if ((j != openedDoor) and (j != firstChoice)): secondChoice = j
      # Note that exactly one choice of i should set second_choice

      if (prnt):
        stdio.write("winning_door=" + str(winningDoor) 
                         + " first_pick=" + str(firstChoice)
                         + " opened_door=" + str(openedDoor)
                         + " other_choice=" + str(secondChoice) + " ")
      
      if (winningDoor == firstChoice):
        if (prnt): stdio.writeln("First pick wins!")
        nStayWins+=1

      if (winningDoor == secondChoice):
        if (prnt): stdio.writeln("Other choice wins!")
        nChangeWins+=1
    
    probWinStay = nStayWins/n
    probWinChange = nChangeWins/ n
    stdio.writeln("Probability of win if stays:" + str(probWinStay));  
    stdio.writeln("Probability of win if changes:" + str(probWinChange));  

if __name__=='__main__': main()
