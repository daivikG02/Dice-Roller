import random
min = 1
max = 6
roll_again = "yes"
while roll_again == "yes" or "y" :
  print ("Rolling the dice....")
  print ("The values are - ")
  print (random.randint (min,max))
  print (random.randint (min,max))
  roll_again = input("Roll the dices again??")