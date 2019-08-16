# Traditional Rock - Paper - Scissors - Game
# Against Computer

import random

ties = 0
wins = 0
losts = 0
rounds = 0

while True:
	ihminen = input("Rock, Paper or Scissors? (Or Quit): ")
	if ihminen == "Quit" or ihminen == "quit":
		print("You played",rounds,"rounds: won",wins,", lost",losts,"and it was a tie",ties,"times.")
		break
	elif ihminen == "Rock" or ihminen == "Paper" or ihminen == "Scissors":
		rounds = rounds + 1
		print("You chose: ",ihminen)
	
		tietokoneenvalinta = random.randint(0,2)
		if tietokoneenvalinta == 0:
			tietokone = "Rock"
		elif tietokoneenvalinta == 1:
			tietokone = "Paper"
		else:
			tietokone = "Scissors"
		print("Computer chose: ",tietokone)
	
		if ihminen == tietokone:
			print("It's a tie!")
			ties = ties + 1
		if (ihminen == "Rock") and (tietokone == "Paper"):
			print("You lost!")
			losts = losts + 1
		if (ihminen == "Rock") and (tietokone == "Scissors"):
			print("You win!")
			wins = wins + 1
		if (ihminen == "Paper") and (tietokone == "Rock"):
			print("You win!")
			wins = wins + 1
		if (ihminen == "Paper") and (tietokone == "Scissors"):
			print("You lost!")
			losts = losts + 1
		if (ihminen == "Scissors") and (tietokone == "Rock"):
			print("You lost!")
			losts = losts + 1
		if (ihminen == "Scissors") and (tietokone == "Paper"):
			print("You win!")
			wins = wins + 1
	else:
		print("Unkown choice.")
