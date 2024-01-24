import random
while True:
  x = int(input("Guess a number:"))
  a=int(input("Enter the lower limit:"))
  b=int(input("Enter the upper limit:"))
  if x == random.randint(a,b):
    print("You guessed right.")
    break 
    exit()
  else:
    print("You guessed wrong.Try again.")
