#Modules
from colorama import Fore, init
init(autoreset=True)
#Hangman
def stage9():
	print()
	print()
	print()
	print()
	print()
	print("|")
def stage8():
	print("__")
	print("|/")
	print("|")
	print("|")
	print("|")
	print("|")
def stage7():
	print("_________")
	print("|/")
	print("|")
	print("|")
	print("|")
	print("|")
def stage6():
	print("_________")
	print("|/	 |")
	print("|")
	print("|")
	print("|")
	print("|")
def stage5():
	print("_________")
	print("|/	 |")
	print("|	 O")
	print("|")
	print("|")
	print("|")
def stage4():
	print("_________")
	print("|/	 |")
	print("|	 O")
	print("|	/|")
	print("|")
	print("|")
def stage3():
	print("_________")
	print("|/	 |")
	print("|	 O")
	print("|	/|\\")
	print("|")
	print("|")
def stage2():
	print("_________")
	print("|/	 |")
	print("|	 O")
	print("|	/|\\")
	print("|	/ ")
	print("|")
def stage1():
	print("_________")
	print("|/	 |")
	print("|	 O")
	print("|	/|\\")
	print("|   / \\")
	print("|")
def stage0():
	print("_________")
	print("|/	 |")
	print("|	 O")
	print("|	/|\\")
	print("|   / \\")
	print("|    *")
def checkstage(chances):
	if chances == 9:
		stage9()
	if chances == 8:
		stage8()
	if chances == 7:
		stage7()
	if chances == 6:
		stage6()
	if chances == 5:
		stage5()
	if chances == 4:
		stage4()
	if chances == 3:
		stage3()
	if chances == 2:
		stage2()
	if chances == 1:
		stage1()
#TicTacToe
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
def single_game():
	values = [' ' for x in range(9)]
	player_pos = {'X':[], 'O':[]}
	i = 0
	alrfill = False
	global player1, player2, cur_Player, player_choice
	curPlayer = player1
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
				if player_choice['X'] == player1:
					player = player2
				elif player_choice['X'] == player2:
					player = player1
		else:
				cur_player = 'X'
#Number21
def nearestmultiple(num):
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
