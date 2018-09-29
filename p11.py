import random
print("lets play the game")
def computer():
	number=random.randint(1,3):
	 if (computer == 0):
	 	computer = "Rock";
    elif (computer == 1):
      	 computer = "Paper";
    elif (computer == 2):
      	 computer = "Scissors";
player=input("enter 1 for rock,2 for paper,3 for scissors")
	if player==computer:
		print("Tie!")
	elif player=="rock":
		if computer=="paper":
			print("you loose",computer,"covers",player)
		else:
			print("you win",player,"smashes",computer )
	elif player=="scissor":
		if computer=="paper":
			print("you win ",player,"cuts",computer)
		else:
			print("you loose",computer,"covers",player)
	elif player=="rock":
		if computer=="scissor":
			print("you loose",computer,"cuts",player)
		else:
			print("you win",player,"smashes",computer)
	else:
		print("invalid input")