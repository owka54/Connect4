# Defines the game board and the column numbers list 
column_nums = [1, 2, 3, 4, 5, 6, 7]
game_board = [["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""]]

# Displays the game board 
def display_board(column_nums, game_board):
  for i in range(len(game_board)):
    print(game_board[i])

# Places a piece on the board and checks if column is full
def place_a_piece(column, game_piece):
    column_full = False
    if 1 <= column <= 7:
        column = column - 1
        if game_board[0][column] != "":
            print("Column is full!")
            column_full = True
        if game_piece == "X" or game_piece == "O":
            for row in reversed(game_board):
                if row[column] == "":
                    row[column] = game_piece
                    break
        else:
            print("Please select either 'X' or 'O' as your game piece.")
    else:
        print("Please select a column between 1 and 7.")
    return column_full

# Checks if the game is over by either a win or a draw
def is_game_over(game_board):
    game_over = False
    # Checks if board is full (no valid moves left)
    if "" not in game_board[0]:
        game_over = True
        print("The game has ended as a draw.")
    # Checks if 'O' has won
    if has_won_row(game_board, "O") == True:
        game_over = True
    if has_won_col(game_board, "O") == True:
        game_over = True
    if has_won_diag(game_board, "O") == True:
        game_over = True
    # Checks if 'X' has won
    if has_won_row(game_board, "X") == True:
        game_over = True
    if has_won_col(game_board, "X") == True:
        game_over = True
    if has_won_diag(game_board, "X") == True:
        game_over = True
    return game_over

# Checks to see if someone has won by 4 in a row -
def has_won_row(game_board, piece):
  x = 0
  for row in game_board:
    for i in row:
      if i == piece:
        x += 1
        if x == 4:
          return True
      else:
        x = 0

# Checks to see if someone has won by 4 in a column |
def has_won_col(game_board, piece):
  x = 0
  col = 0
  while col <= 6:
    for row in game_board:
      if row[col] == piece:
        x += 1
        if x == 4:
          return True
      else:
        x = 0
    col += 1

# Checks to see if someone has won diagonally
def has_won_diag(game_board, piece):
    columns = len(game_board[0])
    rows = len(game_board)
    # Checks \ diagonal 
    for i in range(columns - 3):     
        for e in range(rows - 3):  
            if game_board[e][i] == piece and game_board[e+1][i+1] == piece and game_board[e+2][i+2] == piece and game_board[e+3][i+3] == piece:
                return True
    # Checks / diagonal
    for i in range(3, columns): 
        for e in range(rows - 3):
            if game_board[e][i] == piece and game_board[e+1][i-1] == piece and game_board[e+2][i-2] == piece and game_board[e+3][i-3] == piece:
                return True

# Makes the game playable
def play_game(game_board):
    game_over = False
    column_full = False
    # Loops game until someone wins or it is a draw
    while game_over == False:
        display_board(column_nums, game_board)
        # 'X's turn
        piece = "X"
        col = int(input("'X' it's your turn. Please select where to place your piece (1, 2, 3, 4, 5, 6, 7) "))
        while not 1 <= col <= 7:
            col = int(input("'X' it's your turn. Please select where to place your piece (1, 2, 3, 4, 5, 6, 7) "))
        column_full = place_a_piece(col, piece)
        # If the column selected is full, asks for another input
        while column_full == True:
            column_full = False
            col = int(input("'"+ piece + "'" + " That column is full. Select another "))
            column_full = place_a_piece(col, piece)
        # Check if game is over
        game_over = is_game_over(game_board)
        if game_over == True:
            display_board(column_nums, game_board)
            print(piece + " wins!")
            break

        display_board(column_nums, game_board)
        # 'O's turn
        piece = "O"
        col = int(input("'O' it's your turn. Please select where to place your piece (1, 2, 3, 4, 5, 6, 7) "))
        while not 1 <= col <= 7:
            col = int(input("'O' please choose a valid column (1, 2, 3, 4, 5, 6, 7) "))
        column_full = place_a_piece(col, piece)

        while column_full == True:
            column_full = False
            col = int(input("'"+ piece + "'" + " That column is full. Select another "))
            column_full = place_a_piece(col, piece)

        game_over = is_game_over(game_board)
        if game_over == True:
            display_board(column_nums, game_board)
            print(piece + " wins!")
            break
    print("Thanks for playing!")


play_game(game_board)