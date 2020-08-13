import ast

# difficulty levels for the game
difficultyPool = ("easy", "normal", "hard", "impossible")

# dictionary that associates a level of difficulty to 
# the proper range of guess, the number of attempts and
# the maximum value that a secret number can get
# format of dictionary : difficulty - range, attempts, maximum number
mode = {
	
	"easy" : (20, 4, 99),
	"normal" : (100, 6, 999),
	"hard" : (500, 8, 999),
	"impossible" : (1000, 9, 9999)
}

#displaying the default welcoming message
def welcomingMessage():
	
	try:
		welcomeFile = open("..\\data\\welcomingMessage.txt", "r")
	except:
		welcomeFile = open("data\\welcomingMessage.txt", "r")

	welcomeMessage = welcomeFile.read()
	welcomeFile.close()
	print(welcomeMessage)

# record the play again decision
def waitOnReplay():
	retry = None
	while True:
		retry = input("Would you like to play again? (yes/no)\n")
		if retry == "yes":
			print("Great!")
			break
		elif retry == "no":
			print("Well, see ya then!")
			break
		else:
			print("I'm afraid I can't understand you, please tell me yes or no.")

	return retry

# present the set of rules to the player
def displayRules():
	
	try:
		rulesFile = open("..\\data\\rules.txt", "r")
	except:
		rulesFile = open("data\\rules.txt", "r")
	rulesMessage = rulesFile.read()
	rulesFile.close()
	print(rulesMessage)

#displayes the help guide of the the game
def displayHelp():
	try:
		helpFile = open("..\\help.txt", "r")
	except:
		helpFile = open("help.txt", "r")
	
	helpMessage = helpFile.read()
	print(helpMessage)
	helpFile.close()

# displayes the Highscore table to the user
def displayHighscoreBoard():
	highscoreDict = readHighscoreFile()

	board = None
	while True:
		print("What leaderboard are you interested in?")
		difficultyRequested = input("(easy, normal, hard, impossible)\n")

		if difficultyRequested in ("easy", "normal", "hard", "impossible"):
			board = highscoreDict[difficultyRequested]
			break
		else:
			print("I'm afraid I did not get that.")

	if board[1][0] == '-':
		print("Nobody registered their highscore yet for this difficulty.")
	else:
		print("Place | Name             | Attempts")
		for index in board:
			if board[index][0] == '-':
				break
			#print(str(index) + ".", board[index][0], str(board[index][1]))
			print("{:5.5} | {:16.16} | {}".format(str(index) + ".", board[index][0], str(board[index][1])))

# hints to display for the player
# start and end represent the interval in which the number was choosen
# attempts represents the number of trie to give to the player
def generatedInformation(start, end, attempts):
	print("The number has been choosen. It is a natural number between {} and {}.".format(start, end))
	print("You have {} attempts to guess the number.".format(attempts))
	print("Now let's see if you can guess it.")

# message to display when losing the game
# number reveals the secret random number to the player
def failureMessage(number):
	print("I'm sorry, maybe you need more training or luck.")
	print("The number to be guessed was {}.".format(number))

# sets the difficuly of the game based on player input
def setDifficulty():
	while True:

		print("Choose the desired difficulty to play:")
		difficulty = input("(easy, normal, hard, impossible)\n")
		
		if difficulty not in difficultyPool:
			print("Please try again, you misspelled the difficulty.")
		else:
			try:
				difficultyFile = open("..\\data\\difficulty.txt", "w")
			except:
				difficultyFile = open("data\\difficulty.txt", "w")

			difficultyFile.write(difficulty)
			difficultyFile.close()
			print("Difficulty successfully changed to {}.".format(difficulty))
			break

# gets the default difficulty from the difficulty.txt file
def getDifficulty():
	try:
		difficultyFile = open("..\\data\\difficulty.txt", "r")
	except:
		difficultyFile = open("data\\difficulty.txt", "r")

	difficulty = difficultyFile.read()
	difficultyFile.close()

	return difficulty

# reads the highscore file and returns a dictionary containing
# highscore information
def readHighscoreFile():
	try:
		highscoreFile = open("..\\data\\highscore.txt", "r")
	except:
		highscoreFile = open("data\\highscore.txt", "r")
	
	highscoreString = highscoreFile.read()
	highscoreFile.close()

	highscoreDict = ast.literal_eval(highscoreString)

	return highscoreDict

# receives as input a dicitionary containing the highscore board
# writes the new highscore board to the file
def writeHighscoreFile(highscore):
	while True:

		try:
			highscoreFile = open("..\\data\\highscore.txt", "w")
		except:
			highscoreFile = open("data\\highscore.txt", "w")
		break

		if highscoreFile == None:
			print("Error : Please close the highscore.txt file on your computer.")
			print("Then retry to register your highscore.")
			
			while True:
				response = input("Ready? (yes, when you successfully closed the file)\n")
				if response == "yes":
					break
	highscoreFile.write(str(highscore))

	highscoreFile.close()

	print("Congratulations, you're on the leaderboards!")

# returns true if the comparison of the highscore file
# and the template highscore file has as result an equality
# false otherwise
def isHighscoreFileEmpty():
	try:
		highscoreFile = open("..\\data\\highscore.txt", "r")
	except:
		highscoreFile = open("data\\highscore.txt", "r")

	highscoreString = highscoreFile.read()

	highscoreFile.close()

	return len(highscoreString) == 0

# deletes all the highscores recorded in the highscore.txt
# file by replacing its content with the template located
# in the highscoreTemplate.txt
def eraseHighscoreFile(display):
	
	try:
		try:
			template = open("..\\data\\highscoreTemplate.txt", "r")
			highscoreFile = open("..\\data\\highscore.txt", "w")
		except:
			template = open("data\\highscoreTemplate.txt", "r")
			highscoreFile = open("data\\highscore.txt", "w")
		templateString = template.read()

		highscoreFile.write(templateString)

		template.close()
		highscoreFile.close()

		if display:
			print("All recorded highscores have been removed successfully.")
	except:
		print("An error occured, please restart the game.")


# the process in which the player tries to guess the secret number
# returns a boolean that is used to check if the number was guessed
# and a number which represents the score (number of attemps at guessing
# used by the player)
def guessingProcess(attempts, secretNumber):
	guessed = False
	tries = attempts
	for guess in range(1, attempts + 1):
		
		while True:
			try:
				numberGiven = int(input("Make your choice: ({} more attempts)\n".format(attempts + 1 - guess)))
				break
			except ValueError:
				print("Non numbers values are not accepted, please retry.")

		if numberGiven == secretNumber:
			print("Congratulations, you guessed it in {} attempts.".format(guess))
			guessed = True
			tries = guess
			break
		elif guess < attempts:
			if numberGiven < secretNumber:
				print("The secret number is greater.")
			else:
				print("The secret number is lower.")

	return guessed, tries

# this function copies the highscore file content into a dictionary
# then modifies it in order to include the new record inside it
# as parameters : difficulty will select which leaderboard needs to be modified
# and attempts will be the new record established by the player
# returns the hole new dictionary of highscores 
def recordHighscore(difficulty, attempts):

	highscoreBoards = readHighscoreFile()
	highscoreDict = highscoreBoards[difficulty]

	stack = []

	key = 5 
	while key > 0 and attempts < highscoreDict[key][1]:
		if highscoreDict[key][0] != '-':
			stack.append(highscoreDict[key])
		key -= 1

	if key < 5:
		print("Your score is eligible for leaderboards recording.")
		while True:
			name = input("Please give me your name to put it in the hall of fame:\n(max 16 characters)\n")
			if name == "-" or len(name) > 16:
				print('The provided name is no a legal one, please input another.')
			else:
				break

		highscoreDict[key + 1] = (name, attempts)

		key += 2
		while stack and key < 6:
			highscoreDict[key] = stack.pop(-1)
			key += 1

		highscoreBoards[difficulty] = highscoreDict
	else:
		highscoreBoards = None

	del stack

	return highscoreBoards