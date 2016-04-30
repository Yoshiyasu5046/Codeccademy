# This is the code for Rock, Paper, Scissors!

from random import randint
from time import sleep

options = ["R", "P", "S"]
LOST_MESSAGE = "You lost!"
WINNING_MESSAGE = "You won!"

def decide_winner(user_choice, computer_choice):
	print "You selected: %s" % (user_choice)  
	print "Computer selected: %s" % (computer_choice)
	user_choice_index = options.index(user_choice)
	computer_choice_index = options.index(computer_choice)
  
	if user_choice_index == computer_choice_index:
		print "tie"
	elif user_choice_index == 0 and computer_choice_index == 2:
		print WINNING_MESSAGE
	elif user_choice_index == 1 and computer_choice_index == 0:
		print WINNING_MESSAGE
	elif user_choice_index == 2 and computer_choice_index == 1:
		print WINNING_MESSAGE
	elif user_choice_index > 2:
		print 'Error! Users are supposed to choose either one from the options'
	else:
		print LOST_MESSAGE
		return

def play_RPS():  
	print "Rock, Paper, Scissors?"
	user_choice = raw_input("Select R for Rock, P for Paper, or S for Scissors:").upper()
	sleep(1)
	computer_choice = options[randint(0, len(options)-1)]
	decide_winner(user_choice, computer_choice)
  
play_RPS()