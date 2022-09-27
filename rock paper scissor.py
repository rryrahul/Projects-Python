#rock paper and scissor (Version 1  27/9/2022)
import random

def gameWin(comp,You):
    #if values are equal, declare a tie
    if comp == You:
        return None  
#choose all possibilities of Rock
    elif comp == 'r':
        if You == 's':
            return False
        elif You == 'p':
            return True

#choose all possibilities of Paper
    elif comp == 'p':
        if You == 's':
            return False
        elif You == 'r':
            return True

#choose all possibilities of Scissor
    elif comp == 's':
        if You == 'r':
            return True
        elif You == 'p':
            return False

print("Computer's turn:")
randoNo = random.randint(1,3)
if randoNo == 1:
    comp ='r'
elif randoNo == 2:
    comp = 'p'
elif randoNo == 3:
    comp = 's'

You = input("Player's turn: Rock, paper or  scissor?")
x = gameWin(comp, You)

print(f"Computer chose {comp}")
print(f"You chose {You}")

if x == None:
    print("The game is a tie!")
elif x:
    print("You Win!")
else:
    print("You Lose!")