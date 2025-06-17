import random

num = random.randint(1, 10)
i = 0


while i < 3  :
    guess = int(input("guess a number between 1 and 10: "))
    if i!=2 and guess != num:
     print("Guess again")
     i = i+1
    elif guess == num:
     print("Congratulations !! You guessed right number in  " +str(i+1)+" guess/es.")
     break
    else:
     print("You guessed wrong")
     i = i+1

6