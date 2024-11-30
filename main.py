def interviewer():
	print("\nInterviewer!\n")
	print("What is your name?")
	name = input("} ")
	print("Where do you live?")
	house = input("} ")
	print("What is your favorite color?")
	color = input("} ")
	print("What pet do you have?")
	print("(e.g. I have a cat)")
	print("(e.g. I don't have a pet)")
	pet = input("} ")
	print("How many siblings do you have?")
	siblings = input("} ")
	print("How old are you?")
	age = input("} ")
	print("I speak ___")
	languages = input("} ")
	print("What is your favorite subject at school?")
	subject = input("} ")
	print("What is your favorite hobby?")
	hobby = input("} ")
	print("Where are you from?")
	where_from = input("} ")
	intro = f'''My name is {name}. I am {age} years old. My favorite color is {color}. I am from {where_from} and I speak {languages}. I like {hobby} and my favorite subject is {subject}. I live in {house}, {pet} and {siblings} siblings.'''
	print()
	print()
	print("Hello!")
	print(intro)
	print("Thank you,")
	print(name)
def quiz():
	from colorama import Fore, init
	init(autoreset=True)
	print("\nQuiz!\n")
	print("How many colors in the rainbow?")
	a1 = input("} ")
	if "7" in a1:
		print(Fore.GREEN + "\nGood job!\n")
		print("What is the first president of the United States of America?")
		a2 = input("} ")
		if "washington" in a2.lower():
			print(Fore.GREEN + "\nNice!\n")
			print("How many stars on the US flag?")
			a3 = input("} ")
			if "50" in a3:
				print(Fore.GREEN + "\nGreat!\n")
				print(Fore.GREEN + "You completed the quiz!")
			else:
				print(Fore.RED + "\nIncorrect.")
		else:
			print(Fore.RED + "\nIncorrect.")
	else:
		print(Fore.RED + "\nIncorrect.")
def username_generator():
	import random
	print("\nUsername generator!\n")
	print("No spaces please\n")
	print("Name?")
	name = input("} ")
	print("Number?")
	number = input("} ")
	print("Celebrity?")
	celebrity = input("} ")
	print("Hobby?")
	hobby = input("} ")
	ran = [name, number, celebrity, hobby]
	r1 = random.choice(ran)
	r2 = random.choice(ran)
	r3 = random.choice(ran)
	r4 = random.choice(ran)
	r5 = random.choice(ran)
	r6 = random.choice(ran)
	ra1 = f"{r1}{r2}{r3}"
	ra2 = f"{r4}{r5}{r6}"
	print()
	print(ra1)
	print(ra2)
def calculator():
	import math
	print("\nCalculator!\n")
	from colorama import Fore, init
	init(autoreset=True)

	def add(num1, num2):
		return num1 + num2
	def subtract(num1, num2):
		return num1 - num2
	def multiply(num1, num2):
		return num1 * num2
	def divide(num1, num2):
		return num1 / num2
	def exponent(num1, num2):
		return pow(num1, num2)
	def squarert(num1):
		return math.sqrt(num1)
	print("Select an operation:")
	print("1. add")
	print("2. substract")
	print("3. multiply")
	print("4. divide")
	print("5. exponent")
	print("6. square root")
	select = input("Mode # } ")
	while True:
		if select.isdigit():
			selectint = int(select)
			if selectint < 7 and selectint > 0:
				break
		print("1, 2, 3, 4, 5, 6, 7 please")
		select = input("Mode # } ")
	if selectint == 1:
		number_1 = int(input("Enter first number: "))
		number_2 = int(input("Plus: "))
		print(number_1, "+", number_2, "=", add(number_1, number_2))
	elif selectint == 2:
		number_1 = int(input("Enter first number: "))
		number_2 = int(input("Minus: "))
		print(number_1, "-", number_2, "=", subtract(number_1, number_2))
	elif selectint == 3:
		number_1 = int(input("Enter first number: "))
		number_2 = int(input("Times: "))
		print(number_1, "*", number_2, "=", multiply(number_1, number_2))
	elif selectint == 4:
		number_1 = int(input("Enter first number: "))
		number_2 = int(input("Divided by: "))
		try:
			resultdivision = divide(number_1, number_2)
			print(number_1, "/", number_2, "=", resultdivision)
		except ZeroDivisionError:
			print(Fore.RED + "\nYou can't divide by zero!")
	elif selectint == 5:
		number_1 = int(input("Enter first number: "))
		number_2 = int(input("To the power of: "))
		print(number_1, "^", number_2, "=", exponent(number_1, number_2))
	elif selectint == 6:
		number_1 = int(input("Enter a number: "))
		try:
			print("√", number_1, "=", math.sqrt(number_1))
		except ValueError:
			print(Fore.RED + "\nInvalid input")
	else:
		print(Fore.RED + "\nInvalid input")
def number_guesser():
	import random
	from colorama import Fore, init
	init(autoreset=True)
	attempts = 0
	tries_allowed = 10
	print("\nNumber guesser!\n")
	print("Guess a number between 1 and 20.")
	random_number = random.randint(1, 20)
	while attempts < 10:
		guess = int(input("Please guess a number: "))
		if guess > 20 or guess < 1:
			print("Invalid amount")
		elif guess > random_number:
			print(Fore.LIGHTRED_EX + "Too high, try a smaller number")
			attempts += 1
		elif guess < random_number:
			print(Fore.LIGHTRED_EX + "Too low, try a higher number")
			attempts += 1
		elif guess == random_number:
			attempts += 1
			attempts_used = str(attempts)
			print(Fore.GREEN + f"Correct! you win in {attempts_used} guesses")
			break
	else:
		if tries_allowed == 10:
			print(Fore.RED + "You failed to guess in time")
def hangman():
	import random
	from hangman import stage0, checkStage
	from collections import Counter
	from colorama import Fore, init
	init(autoreset=True)
	print("\nHangman!\n")
	print("Do you want to access hard mode?")
	hardmode = input("} ")
	if "yes" in hardmode.lower():
		print("Entering hard mode...")
		hardWords = '''anemone syzygy fjord zephyr'''
		HardWords = hardWords.split(" ")
		hardword = random.choice(HardWords)
		print("Hangman!")
		letterGuessed = ""
		LetterGuessed = ""
		chances = len(hardword) + 2
		chances = chances
		correct = 0
		flag = False
		tries = 0
		win = False
		checkStage(chances)
		for i in hardword:
			print("_", end=" ")
		print()
		try:
			while (chances != 0) and not flag:
				print()
				tries += 1
				try:
					guess = str(input("Enter a letter to guess: "))
				except ValueError:
					print(Fore.RED + "Enter only a letter!")
					continue
				if not guess.isalpha():
					print(Fore.RED + "Enter only a letter!")
					continue
				elif guess == hardword:
					win = True
					break
				elif len(guess) > 1:
					print(Fore.RED + "That is not the word")
					chances -= 1
					checkStage(chances)
					continue
				elif guess in LetterGuessed:
					print(Fore.RED + "You have already guessed that letter")
					continue
				if guess in hardword:
					checkStage(chances)
					k = hardword.count(guess)
					for _ in range(k):
						letterGuessed += guess
						LetterGuessed += guess
				else:
					LetterGuessed += guess
					print("Wrong!")
					print("Remaining tries:")
					chances -= 1
					print(chances)
					checkStage(chances)
				for char in hardword:
					if char in letterGuessed and (Counter(letterGuessed)  != Counter(hardword)):
						print(char, end=" ")
						correct += 1
					elif (Counter(letterGuessed) == Counter(hardword)):
						print("The word is: ", end = "")
						print(hardword)
						print(Fore.GREEN + "\nCongratulations, You won!\n")
						print(Fore.GREEN + "You guessed the word in " + Fore.GREEN + str(tries) + Fore.GREEN + " tries")
						win = True
						break
					else:
						print("_", end=" ")
				if (Counter(letterGuessed) == Counter(hardword)):
					break
			if not win:
				stage0()
				print(Fore.RED + "\nYou lost! Try again..\n")
				print(Fore.RED + "The word was " + Fore.GREEN + "{}".format(hardword))

		except KeyboardInterrupt:
			print()
			print(Fore.RED + "Bye! Try again.")
			exit()
	elif "no" in hardmode.lower():
		easyWords = "school life bus cats house grape pencil teacher"
		EasyWords = easyWords.split(" ")
		easyword = random.choice(EasyWords)
		print("\nHangman!\n")
		letterGuessed = ""
		LetterGuessed = ""
		chances = len(easyword) + 2
		chances = chances
		correct = 0
		flag = False
		tries = 0
		win = False
		checkStage(chances)
		for i in easyword:
			print("_", end=" ")
		print()
		try:
			while (chances != 0) and not flag:
				print()
				tries += 1
				try:
					guess = str(input("Enter a letter to guess: "))
				except ValueError:
					print(Fore.RED + "Enter only a letter!")
					continue
				if not guess.isalpha():
					print(Fore.RED + "Enter only a letter!")
					continue
				elif guess == easyword:
					win = True
					break
				elif len(guess) > 1:
					print(Fore.RED + "That is not the word")
					chances -= 1
					checkStage(chances)
					continue
				elif guess in LetterGuessed:
					print(Fore.RED + "You have already guessed that letter")
					continue
				if guess in easyword:
					checkStage(chances)
					k = easyword.count(guess)
					for _ in range(k):
						letterGuessed += guess
						LetterGuessed += guess
				else:
					LetterGuessed += guess
					print("Wrong!")
					print("Remaining tries:")
					chances -= 1
					print(chances)
					checkStage(chances)
				for char in easyword:
					if char in letterGuessed and (Counter(letterGuessed) != Counter(easyword)):
						print(char, end=" ")
						correct += 1
					elif (Counter(letterGuessed) == Counter(easyword)) or win is True:
						print("The word is: ", end="")
						print(easyword)
						flag = True
						print(Fore.GREEN + "\nCongratulations, You won!\n")
						print(Fore.GREEN + "You guessed the word in " + Fore.GREEN + str(tries) + Fore.GREEN + " tries")
						break
					else:
						print("_", end=" ")
			if chances <= 0 and (Counter(letterGuessed) != Counter(easyword)):
				stage0()
				print(Fore.RED + "\nYou lost! Try again..\n")
				print(Fore.RED + "The word was " + Fore.GREEN + "{}".format(easyword))

		except KeyboardInterrupt:
			print()
			print(Fore.RED + "Bye! Try again.")
			exit()
	elif Counter(letterGuessed) == Counter(hardword) or Counter(letterGuessed) == Counter(easyword):
		pass
	else:
		print(Fore.RED + "\nInvalid input")
def number_21():
	from colorama import Fore, init
	init(autoreset=True)
	def nearestMultiple(num):
		if num >= 4:
			near = num + (4 - (num % 4))
		else:
			near = 4
		return near
	def lose1():
		print (Fore.RED + "\nYou lose!")
		exit(0)
	def check(xyz):
		i = 1
		while i<len(xyz):
			if (xyz[i]-xyz[i-1])!= 1:
				return False
			i = i + 1
		return True
	def start1():
		print("The number 21 game!")
		xyz = []
		last = 0
		while True:
			print ("\nEnter 1 to play first.")
			print("\nEnter 2 to play second.")
			turn = input("} ")
			if turn == "1":
				while True:
					if last == 20:
						lose1()
					else:
						print ("\nYour Turn.")
						print ("\nHow many numbers do you wish to enter?")
						try:
							inp = int(input("} "))
						except ValueError:
							print(Fore.RED + "\nInvalid input")
							win = False
							break
						if inp > 0 and inp <= 3:
							comp = 4 - inp
						else:
							print (Fore.RED + "\nInvalid input")
							win = False
							break
						i, j = 1, 1
						print ("\nNow enter the values")
						while i <= inp:
							a = input("} ")
							try:
								a = int(a)
							except ValueError:
								print(Fore.RED + "Invalid input")
								win = False
								break
							if a != (last+i):
								print (Fore.RED + "\nInvalid input")
								win = False
								break
							xyz.append(a)
							i = i + 1
						try:
							last = xyz[-1] 
						except IndexError:
							win = False
							break
						if check(xyz) is True: 
							if last == 21:
								lose1()
							else:
								while j <= comp:
									xyz.append(last + j)
									j = j + 1
								print ("\nOrder of inputs after computer's turn is: ")
								print (xyz)
								last = xyz[-1]
						else:
							print ("\nYou did not input consecutive integers.")
							lose1()
			elif turn == "2":
				comp = 1
				last = 0
				win = True
				while last < 20:
					j = 1
					while j <= comp:
						xyz.append(last + j)
						j = j + 1
					print ("\nOrder of inputs after computer's turn is:")
					print (xyz)
					if xyz[-1] == 20:
						lose1()

					else:
						print ("\nYour turn.")
						print ("\nHow many numbers do you wish to enter?")
						try:
							inp = int(input("} "))
						except ValueError:
							print(Fore.RED + "\nInvalid input")
							win = False
							break
						if inp > 0 and inp <= 3:
							comp = 4 - inp
						else:
							print (Fore.RED + "\nInvalid input")
							win = False
							break
						i, j = 1, 1
						print ("Enter your values")
						while i <= inp:
							xyz.append(int(input("} ")))
							i = i + 1
						last = xyz[-1]
						if check(xyz) is True:
							near = nearestMultiple(last)
							comp = near - last
							if comp == 4:
								comp = 3
							else:
								comp = comp
						else:
							print ("\nYou did not input consecutive integers.")
							lose1()
				if win is not False:
					print (Fore.GREEN + "\nCONGRATULATIONS!")
					print (Fore.GREEN + "\nYOU WON!")
					break
			else:
				print (Fore.RED + "\nInvalid input")
	start1()
def credit():
	credits = [
	    "Debugging:", "", "Geeksforgeeks", "Teddy Millot", "Mary Jo Armen",
	    "W3schools", "Stackoverflow", "", "Teaching:", "", "Mary Jo Armen",
	    "Teddy Millot", "Geeksforgeeks", "W3schools", "",
	    "Compiler/Interpretor:", "", "Replit", "Hello World", "W3schools\n"
	]
	for x in credits:
		print(x)
def start_game():
	from colorama import Fore, init
	init(autoreset=True)
	from functions import interviewer, quiz, username_generator, calculator, number_guesser, hangman
	print(Fore.GREEN + "Python")
	print("By " + Fore.YELLOW + "Tao Millot")

	while True:
		print()
		print("Choose one:")
		print("1. interviewer")
		print("2. quiz")
		print("3. username generator")
		print("4. calculator")
		print("5. number guesser")
		print("6. hangman")
		print("7. number 21 game")
		print("8. exit")
		mode = input("Mode # } ")
		if mode == "8":
			print(Fore.LIGHTRED_EX + "Are you sure?")
			exit1 = input("} ")
			if "yes" in exit1.lower():
				exit()
			else:
				continue
		while True:
			if not mode.isdigit():
				if "credit" in mode:
					break
			if mode.isdigit():
				modeint = int(mode)
				if modeint < 9 and modeint > 0:
					break
			print(Fore.RED + "\n1, 2, 3, 4, 5, 6, 7, 8, or 9 please\n")
			mode = input("Mode # } ")
		if "1" in mode:
			interviewer()
		if "2" in mode:
			quiz()
		if "3" in mode:
			username_generator()
		if "4" in mode:
			calculator()
		if "5" in mode:
			number_guesser()
		if "6" in mode:
			hangman()
		if "7" in mode:
			number_21()
		if "credit" in mode:
			credit()
start_game()
