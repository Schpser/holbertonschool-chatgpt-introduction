#!/usr/bin/python3
def print_board(board):
	for row in board:
		print(" | ".join(row))
		print("-" * 5)

def check_winner(board):
	# Vérifier les lignes
	for row in board:
		if row.count(row[0]) == len(row) and row[0] != " ":
			return row[0]  # Retourne le joueur gagnant ("X" ou "O")
	
	# Vérifier les colonnes
	for col in range(len(board[0])):
		if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
			return board[0][col]
	
	# Vérifier les diagonales
	if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
		return board[0][0]
	
	if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
		return board[0][2]
	
	return None  # Aucun gagnant

def is_board_full(board):
	# Vérifie si le tableau est complètement rempli
	for row in board:
		if " " in row:
			return False
	return True

def tic_tac_toe():
	board = [[" "]*3 for _ in range(3)]
	player = "X"
	
	while True:
		print_board(board)
		
		# Gestion des entrées utilisateur avec vérification
		try:
			row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
			col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
			
			if row not in [0, 1, 2] or col not in [0, 1, 2]:
				print("Invalid input! Please enter values between 0 and 2.")
				continue
				
		except ValueError:
			print("Invalid input! Please enter numbers only.")
			continue
		
		# Vérifier si la case est libre
		if board[row][col] != " ":
			print("That spot is already taken! Try again.")
			continue
		
		# Placer le pion du joueur
		board[row][col] = player
		
		# Vérifier s'il y a un gagnant
		winner = check_winner(board)
		if winner:
			print_board(board)
			print("Player " + winner + " wins!")
			break
		
		# Vérifier s'il y a égalité
		if is_board_full(board):
			print_board(board)
			print("It's a tie!")
			break
		
		# Changer de joueur
		player = "O" if player == "X" else "X"

tic_tac_toe()
