import random

randm=random.randrange(1,10)
inpt=int(input(' guess a number between 1 and 9:'))
if inpt<randm:
	print('you guessed too low')
elif inpt==randm:
    print('you guessed exactly right')	

else:
   print('you guessed too high')    