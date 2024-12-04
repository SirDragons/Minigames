import random
import math
from functions import stage0, checkstage, lose1, check, nearestmultiple, single_game
from colorama import Fore, init
init(autoreset=True)
letterGuessed = 'a'
hardword = 'ab'
easyword = 'abc'
while True:
	print()
	print('\t ---------------------------')
	print('\t         Minigames          ')
	print('\t ---------------------------')
	print('\t Hangman-----------TicTacToe')
	print('\t Number21---------Calculator')
	print('\t -------NumberGuesser-------')
	print('\t------------Exit------------')
	print()
	leave = False
	mode = input('} ')

	if 'hangman' in mode.lower():
		import random
		from functions import stage0, checkstage
		from collections import Counter
		from colorama import Fore, init
		init(autoreset=True)
		print('\nHangman!\n')
		print('Do you want to access hard mode?')
		hardmode = input('} ')
		if 'yes' in hardmode.lower() and len(hardmode) == 3:
			print('Entering hard mode...')
			hardWords = '''anemone syzygy fjord zephyr'''
			HardWords = hardWords.split(' ')
			hardword = random.choice(HardWords)
			print('Hangman!')
			letterGuessed = ''
			LetterGuessed = ''
			chances = len(hardword) + 2
			chances = chances
			correct = 0
			flag = False
			tries = 0
			win = False
			checkstage(chances)
			for i in hardword:
				print('_', end=' ')
			print()
			try:
				while (chances != 0) and not flag:
					print()
					tries += 1
					try:
						guess = str(input('Enter a letter to guess: '))
					except ValueError:
						print(Fore.RED + 'Enter only a letter!')
						continue
					if not guess.isalpha():
						print(Fore.RED + 'Enter only a letter!')
						continue
					elif guess == hardword:
						win = True
						break
					elif len(guess) > 1:
						print(Fore.RED + 'That is not the word')
						chances -= 1
						checkstage(chances)
						continue
					elif guess in LetterGuessed:
						print(Fore.RED + 'You have already guessed that letter')
						continue
					if guess in hardword:
						checkstage(chances)
						k = hardword.count(guess)
						for _ in range(k):
							letterGuessed += guess
							LetterGuessed += guess
					else:
						LetterGuessed += guess
						print('Wrong!')
						print('Remaining tries:')
						chances -= 1
						print(chances)
						checkstage(chances)
					for char in hardword:
						if char in letterGuessed and (Counter(letterGuessed)  != Counter(hardword)):
							print(char, end=' ')
							correct += 1
						elif (Counter(letterGuessed) == Counter(hardword)):
							print('The word is: ', end = '')
							print(hardword)
							print(Fore.GREEN + '\nCongratulations, You won!\n')
							print(Fore.GREEN + 'You guessed the word in ' + Fore.GREEN + str(tries) + Fore.GREEN + ' tries')
							win = True
							break
						else:
							print('_', end=' ')
					if (Counter(letterGuessed) == Counter(hardword)):
						break
				if not win:
					stage0()
					print(Fore.RED + '\nYou lost! Try again..\n')
					print(Fore.RED + 'The word was ' + Fore.GREEN + '{}'.format(hardword))

			except KeyboardInterrupt:
				print()
				print(Fore.RED + 'Bye! Try again.')
				exit()
		elif 'no' in hardmode.lower() and len(hardmode) == 2:
			easyWords = 'school life bus cats house grape pencil teacher'
			EasyWords = easyWords.split(' ')
			easyword = random.choice(EasyWords)
			print('\nHangman!\n')
			letterGuessed = ''
			LetterGuessed = ''
			chances = len(easyword) + 2
			chances = chances
			correct = 0
			flag = False
			tries = 0
			win = False
			checkstage(chances)
			for i in easyword:
				print('_', end=' ')
			print()
			try:
				while (chances != 0) and not flag:
					print()
					tries += 1
					try:
						guess = str(input('Enter a letter to guess: '))
					except ValueError:
						print(Fore.RED + 'Enter only a letter!')
						continue
					if not guess.isalpha():
						print(Fore.RED + 'Enter only a letter!')
						continue
					elif guess == easyword:
						win = True
						break
					elif len(guess) > 1:
						print(Fore.RED + 'That is not the word')
						chances -= 1
						checkstage(chances)
						continue
					elif guess in LetterGuessed:
						print(Fore.RED + 'You have already guessed that letter')
						continue
					if guess in easyword:
						checkstage(chances)
						k = easyword.count(guess)
						for _ in range(k):
							letterGuessed += guess
							LetterGuessed += guess
					else:
						LetterGuessed += guess
						print('Wrong!')
						print('Remaining tries:')
						chances -= 1
						print(chances)
						checkstage(chances)
					for char in easyword:
						if char in letterGuessed and (Counter(letterGuessed) != Counter(easyword)):
							print(char, end=' ')
							correct += 1
						elif (Counter(letterGuessed) == Counter(easyword)) or win is True:
							print('The word is: ', end='')
							print(easyword)
							flag = True
							print(Fore.GREEN + '\nCongratulations, You won!\n')
							print(Fore.GREEN + 'You guessed the word in ' + Fore.GREEN + str(tries) + Fore.GREEN + ' tries')
							break
						else:
							print('_', end=' ')
				if chances <= 0 and (Counter(letterGuessed) != Counter(easyword)):
					stage0()
					print(Fore.RED + '\nYou lost! Try again..\n')
					print(Fore.RED + 'The word was ' + Fore.GREEN + '{}'.format(easyword))
			except KeyboardInterrupt:
				print()
				print(Fore.RED + 'Bye! Try again.')
				exit()
		elif Counter(letterGuessed) == Counter(hardword) or Counter(letterGuessed) == Counter(easyword):
			leave = True
			continue
		else:
			print(Fore.RED + '\nInvalid input')
	elif 'tictactoe' in mode.lower():
		print('\nTic Tac Toe!\n')
		player1 = input('First player: ')
		print()
		player2 = input('Second player: ')
		print()
		cur_player = player1
		cur_Player = player1
		player = cur_player
		player_choice = {'X' : '', 'O' : ''}
		options = ['X', 'O']
		score_board = {player1: 0, player2: 0}
		def print_tic_tac_toe(values):
			print("\n")
			print("\t     |     |")
			print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
			print('\t_____|_____|_____')
			print("\t     |     |")
			print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
			print('\t_____|_____|_____')
			print("\t     |     |")
			print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
			print("\t     |     |")
			print("\n")
		def print_scoreboard(score_board):
			print("\t---------------------------------------")
			print("\t              SCOREBOARD               ")
			print("\t---------------------------------------")
			players = list(score_board.keys())
			if cur_Player == player1:
				if score_board[players[0]] > score_board[players[1]]:
					print("\t   ", players[0], "\t    ", Fore.GREEN + str(score_board[players[0]]))
					print("\t   ", players[1], "\t    ", Fore.RED + str(score_board[players[1]]))
				elif score_board[players[0]] < score_board[players[1]]:
					print("\t   ", players[0], "\t    ", Fore.RED + str(score_board[players[0]]))
					print("\t   ", players[1], "\t    ", Fore.GREEN + str(score_board[players[1]]))
				else:
					print("\t   ", players[0], "\t    ", score_board[players[0]])
					print("\t   ", players[1], "\t    ", score_board[players[1]])
			elif cur_Player == player2:
				if score_board[players[0]] > score_board[players[1]]:
					print("\t   ", players[0], "\t    ", Fore.GREEN + str(score_board[players[0]]))
					print("\t   ", players[1], "\t    ", Fore.RED + str(score_board[players[1]]))
				elif score_board[players[0]] < score_board[players[1]]:
					print("\t   ", players[0], "\t    ", Fore.RED + str(score_board[players[0]]))
					print("\t   ", players[1], "\t    ", Fore.GREEN + str(score_board[players[1]]))
				else:
					print("\t   ", players[0], "\t    ", score_board[players[0]])
					print("\t   ", players[1], "\t    ", score_board[players[1]])

			print("\t---------------------------------------\n")
		def check_win(player_pos, cur_player):
			soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
			for x in soln:
					if all(y in player_pos[cur_player] for y in x):
							return True
			return False
		def check_draw(player_pos):
			if len(player_pos['X']) + len(player_pos['O']) == 9:
					return True
			return False
		def single_game(cur_player):
			values = [' ' for x in range(9)]
			player_pos = {'X':[], 'O':[]}
			i = 0
			alrfill = False
			curPlayer = player1
			curplayer = player1
			notcurPlayer = player2
			print("\n")
			print("\t     |     |")
			print("\t (1) | (2) | (3)")
			print('\t_____|_____|_____')
			print("\t     |     |")
			print("\t (4) | (5) | (6)")
			print('\t_____|_____|_____')
			print("\t     |     |")
			print("\t (7) | (8) | (9)")
			print("\t     |     |")
			print()
			while True:
				if alrfill is False:
					i += 1
				else:
					pass
				alrfill = False
				if cur_Player == player1:
					if i % 2 == 0:
						curplayer = notcurPlayer
					else:
						curplayer = curPlayer
				elif cur_Player == player2:
					if i % 2 == 0:
						curplayer = curPlayer
					else:
						curplayer = notcurPlayer
				print_tic_tac_toe(values)
				try:
						print(f"Player {curplayer} ({cur_player}) turn. Which box? : ", end="")
						move = int(input())
				except ValueError:
						print(Fore.RED + "\nInvalid input")
						alrfill = True
						continue
				if move < 1 or move > 9:
						print(Fore.RED + "\nInvalid input")
						alrfill = True
						continue
				if values[move-1] != ' ':
						print(Fore.RED + "\nPlace already filled")
						alrfill = True
						continue
				values[move-1] = cur_player
				player_pos[cur_player].append(move)
				if check_win(player_pos, cur_player):
						print_tic_tac_toe(values)
						print(Fore.GREEN + f"{cur_Player} has won the game!")
						print("")
						return cur_player
				if check_draw(player_pos):
						print_tic_tac_toe(values)
						print("Game Drawn")
						print("")
						return 'D'
				if cur_player == 'X' and alrfill is False:
						cur_player = 'O'
				else:
						cur_player = 'X'
		print_scoreboard(score_board)
		while True:
				print('Turn to choose for', cur_player + ':\n')
				print('Enter 1 for X')
				print('Enter 2 for O')
				print('Enter 3 to Quit')
				try:
						choice = int(input('} '))
				except ValueError:
						print(Fore.RED + '\nInvalid input\n')
						continue
				if choice == 1:
						player_choice['X'] = cur_player
						if cur_player == player1:
								player_choice['O'] = player2
						else:
								player_choice['O'] = player1
				elif choice == 2:
						player_choice['O'] = cur_player
						if cur_player == player1:
								player_choice['X'] = player2
						else:
								player_choice['X'] = player1
				elif choice == 3:
						print('Final Scores')
						print_scoreboard(score_board)
						break
				else:
						print(Fore.RED + '\nInvalid input\n')
				try:
					winner = single_game(options[choice-1])
				except IndexError:
					continue
				if winner != 'D' :
						player_won = player_choice[winner]
						score_board[player_won] = score_board[player_won] + 1
				print_scoreboard(score_board)
				if cur_player == player1:
						cur_player = player2
						cur_Player = player2
				else:
						cur_player = player1
						cur_Player = player1
	elif 'number21' in mode.lower():
		print('\nThe number 21 game!\n')
		xyz = []
		last = 0
		while True:
			print ('\nEnter 1 to play first.')
			print('\nEnter 2 to play second.')
			turn = input('} ')
			if turn == '1':
				while True:
					if last == 20:
						lose1()
					else:
						print ('\nYour Turn.')
						print ('\nHow many numbers do you wish to enter?')
						try:
							inp = int(input('} '))
						except ValueError:
							print(Fore.RED + '\nInvalid input')
							win = False
							break
						if inp > 0 and inp <= 3:
							comp = 4 - inp
						else:
							print (Fore.RED + '\nInvalid input')
							win = False
							break
						i, j = 1, 1
						print ('\nNow enter the values')
						while i <= inp:
							a = input('} ')
							try:
								a = int(a)
							except ValueError:
								print(Fore.RED + 'Invalid input')
								win = False
								break
							if a != (last+i):
								print (Fore.RED + '\nInvalid input')
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
							print ('\nYou did not input consecutive integers.')
							lose1()
			elif turn == '2':
				comp = 1
				last = 0
				win = True
				while last < 20:
					j = 1
					while j <= comp:
						xyz.append(last + j)
						j = j + 1
					print ("Order of inputs after computer's turn is:")
					print (xyz)
					if xyz[-1] == 20:
						lose1()

					else:
						print ('\nYour turn.')
						print ('\nHow many numbers do you wish to enter?')
						try:
							inp = int(input('} '))
						except ValueError:
							print(Fore.RED + '\nInvalid input')
							win = False
							break
						if inp > 0 and inp <= 3:
							comp = 4 - inp
						else:
							print (Fore.RED + '\nInvalid input')
							win = False
							break
						i, j = 1, 1
						print ('Enter your values')
						while i <= inp:
							xyz.append(int(input('} ')))
							i = i + 1
						last = xyz[-1]
						if check(xyz) is True:
							near = nearestmultiple(last)
							comp = near - last
							if comp == 4:
								comp = 3
							else:
								comp = comp
						else:
							print ('\nYou did not input consecutive integers.')
							lose1()
				if win is not False:
					print (Fore.GREEN + '\nCONGRATULATIONS!')
					print (Fore.GREEN + '\nYOU WON!')
					break
			else:
				print (Fore.RED + '\nInvalid input')
	elif 'calculator' in mode.lower():
		print('\nCalculator!\n')
		plus = 'Plus'
		Plus = '+'
		minus = 'Minus'
		Minus = '-'
		times = 'Times'
		Times = '*'
		divided = 'Divided by'
		exp = 'To the power of'
		squrt = ''
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
		def squareroot(num1):
			return math.sqrt(num1)
		def playoperation(add, plus, Plus):
			number_1 = int(input('Enter first number: '))
			number_2 = int(input(f'{plus}: '))
			print(number_1, Plus, number_2, '=', add(number_1, number_2))
		def playspecialop(exponent, exp, ex):
			from colorama import Fore, init
			init(autoreset=True)
			if ex == 'ex':
				number_1 = int(input('Enter first number: '))
				number_2 = int(input('To the power of: '))
				print(number_1, '^', number_2, '=', exponent(number_1, number_2))
			if ex == 'di':
				from colorama import Fore, init
				init(autoreset=True)
				number_1 = int(input('Enter first number: '))
				number_2 = int(input('Divided by: '))
				try:
					resultdivision = divide(number_1, number_2)
					print(number_1, '/', number_2, '=', resultdivision)
				except ZeroDivisionError:
					print(Fore.RED + "\nYou can't divide by zero!")
			if ex == 'sq':
				try:
					number_1 = int(input('Enter a number: '))
					print('√', number_1, '=', squareroot(number_1))
				except ValueError:
					print(Fore.RED + '\nInvalid input')
		print('Please select an operation')
		print('1. add')
		print('2. subtract')
		print('3. multiply')
		print('4. divide')
		print('5. exponent')
		print('6. square root')
		select = input('Mode # } ')
		while True:
			if select.isdigit():
				selectint = int(select)
				if selectint < 7 and selectint > 0:
					break
			print(Fore.RED + '\n1, 2, 3, 4, 5, 6, 7 please\n')
			select = input('Mode # } ')
		if selectint == 1:
			playoperation(add, plus, Plus)
		elif selectint == 2:
			playoperation(subtract, minus, Minus)
		elif selectint == 3:
			playoperation(multiply, times, Times)
		elif selectint == 4:
			playspecialop(divide, divided, 'di')
		elif selectint == 5:
			playspecialop(exponent, exp, 'ex')
		elif selectint == 6:
			playspecialop(squareroot, squrt, 'sq')
	elif 'numberguesser' in mode.lower():
		print('\nNumber Guesser!\n')
		attempts = 0
		tries_allowed = 10
		print('\nNumber guesser!\n')
		print('Guess a number between 1 and 20.')
		random_number = random.randint(1, 20)
		while attempts < 10:
			guess = int(input('Please guess a number: '))
			if guess > 20 or guess < 1:
				print('Invalid amount')
			elif guess > random_number:
				print(Fore.LIGHTRED_EX + 'Too high, try a smaller number')
				attempts += 1
			elif guess < random_number:
				print(Fore.LIGHTRED_EX + 'Too low, try a higher number')
				attempts += 1
			elif guess == random_number:
				attempts += 1
				attempts_used = str(attempts)
				print(Fore.GREEN + f'Correct! you win in {attempts_used} guesses')
				break
		else:
			if tries_allowed == 10:
				print(Fore.RED + 'You failed to guess in time')
	elif 'exit' in mode.lower():
		print('Are you sure?')
		rus = input('} ')
		if 'yes' in rus.lower():
			exit()
		else:
			continue
	elif leave:
		continue
	else:
		print(Fore.RED + 'Invalid input')
		print(Fore.RED + 'Please try to spell correctly')
