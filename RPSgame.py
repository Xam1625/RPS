import random

choices = ['ROCK', 'PAPER', 'SCISSORS']					
usr_choice = input("Enter ROCK, PAPER, or SCISSORS:\n").upper()		
com_choice = random.choice(choices)					

while usr_choice not in choices:
	print('You made an invalid choice - Please try again!')
	usr_choice = input("Enter ROCK, PAPER, or SCISSORS:\n").upper()
else:
	print('You chose: ' + usr_choice + '\nComputer chose: ' + com_choice)

	if com_choice == usr_choice:
		print('DRAW')
	elif usr_choice == 'ROCK' and com_choice == 'SCISSORS':
		print('User Wins!')
	elif usr_choice == 'PAPER' and com_choice == 'ROCK':
		print('User Wins!')
	elif usr_choice == 'SCISSORS' and com_choice == 'PAPER':
		print('User Wins!')
	else:
		print('Computer Wins - LOSER!')
