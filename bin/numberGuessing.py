import random as rd
import functionalities as func
import os
import time

def playTheGame():
	
	#choose the difficulty
	difficulty = func.getDifficulty()
	interval, attempts, maximumNumberInGame = func.mode[difficulty]

	while True:
		# the interval of numbers in which the player will try to guess
		startOfInterval = rd.randint(1, maximumNumberInGame - interval)
		endOfInterval = startOfInterval + interval

		# number to be guessed by the player
		secretNumber = rd.randint(startOfInterval, endOfInterval)

		# hints for player
		func.generatedInformation(startOfInterval, endOfInterval, attempts)

		# the process in which the player tries to guess the number
		guessed, tries = func.guessingProcess(attempts, secretNumber)

		# in case of failure display an encouraging message
		if not guessed:
			func.failureMessage(secretNumber)
		else:
			highscoreBoards = func.recordHighscore(difficulty, tries)
			if highscoreBoards:
				func.writeHighscoreFile(highscoreBoards)
		
		# let the player decide if they want to replay	
		retry = func.waitOnReplay()

		if retry == "no":
			break

### START OF EXECUTION

# displays the default welcoming message
func.welcomingMessage()

# if an error occured and the highscore file is empty copies
# in it the contents of the highscoreTemplate.txt file
if func.isHighscoreFileEmpty():
	func.eraseHighscoreFile(False)

#let the player explore the main manu
while True :

	print("You're on the main manu. Please give me your command:")
	request = input("(play, help, rules, highscore, difficulty, reset, clear, exit)\n")

	if request == "play":
		playTheGame()
	elif request == "help":
		func.displayHelp()
	elif request == "rules":
		func.displayRules()
	elif request == "highscore":
		func.displayHighscoreBoard()
	elif request == "difficulty":
		
		diff = func.getDifficulty()
		print("The current difficulty is {}.".format(diff))
		print('Type "change" to set the difficulty, "exit" otherwise.')
		while True:
			answer = input()

			if answer == "change":
				func.setDifficulty()
				break
			elif answer == "exit":
				break
			else:
				print("I'm sorry, I cannot understand that, will you repeat?")
	elif request == "reset":

		print("Are you sure you want to ERASE ALL THE RECORDED HIGHSCORES?")

		response = input("(type YES to confirm)\n")

		if response == "YES":
			func.eraseHighscoreFile(True)
		else:
			print("It appears you changed your mind, good for you!")

	elif request == "clear":
		os.system('cls')
	elif request == "exit":
		print("Well, see ya next time my friend!")
		time.sleep(2) # wait 2 seconds before closing
		break
	else:
		print("I'm sorry, I cannot understand that, will you repeat?")