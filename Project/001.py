# game of guessing

import random

randNum=random.randint(1,100)
print("---GUESS A NUMBER BETWEEN 1 TO 100---")
while True:
    GuessNum=input("enter your guess or Quit(type Q): ")
    if(GuessNum=="Q"):
        print("KAAM NAI BILLA")
        break

    GuessNum=int(GuessNum)
    if(GuessNum > randNum):
        print("Your number is too big,BILLA")
    elif(GuessNum < randNum):
        print("Your number is too small,BILLA")
    else:
        print("YOU'RE CORRECT. 7 CRORE ....")
        break

print("-------GAME OVER----------")