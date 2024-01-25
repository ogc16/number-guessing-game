def rollDice():
  import random
  dice = random.randint(1,6)
  print("You rolled", dice)

x=int(input("How many times do you want to roll the dice?:"))
for i in range(x):
   rollDice()

print("Thanks for rolling the dice!")
