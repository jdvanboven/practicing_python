# grid_width and grid_height determine the size of the playing grid.
grid_width = 7
grid_height = 6

# piece_list keeps track of which pieces have been placed
piece_list = [["-"] * grid_width for i in range(grid_height)]


# The function display_game prints the grid with a size determined by grid_width and grid_height
# The function uses piece_list to display the placed pieces in the grid
def display_game():
    c = 65

    # First row
    print(f"  ", end="")
    for j in range(grid_width):
        print(f"| {j+1} ", end="")
    print("| ")
    print((grid_width * 4 + 4) * "-")

    # Other rows
    for i in range(grid_height):
        print(f"{chr(c+i)} ", end="")
        for j in range(grid_width):
            print(f"| {piece_list[i][j]} ", end="")
        print("| ")
        print((grid_width * 4 + 4) * "-")


# class Counter is used to create a turn counter that keeps track of turn number and current player
class Counter:
    def __init__(self):
        self.turn_number = 1  # The first turn is always 1
        self.player_symbol = "X"  # Player "X" is always the starting player

    def __str__(self):
        return f"It's turn {self.turn_number}. Player {self.player_symbol}, your move!"

    # change_turn is a method to increase turn number and change player after every turn
    def change_turn(self):
        self.turn_number += 1
        if self.player_symbol == "X":
            self.player_symbol = "O"
        else:
            self.player_symbol = "X"

# We create object turn_counter to hold the turn number and current player
turn_counter = Counter()

class Move_details:
    def __init__(self, row, column, symbol):
        self.row = row
        self.column = column
        self.symbol = symbol

    def __str__(self):
        return f"Row {self.row}, column {self.column}, symbol {self.symbol}"
    
    def update_move_details(self, row, column, symbol):
        self.row = row
        self.column = column
        self.symbol = symbol

last_move = Move_details(0, 0, "X")

def player_move(column_number):

    # First, check if a column_number is given that fits on the board
    if 1 <= column_number <= grid_width:

        # Then, go backwards through the following range and look for the first empty space in the selected column
        for a in range(grid_height - 1, -1, -1):

            # If no empty space is found, print a message that the column is full
            if piece_list[0][column_number - 1] != "-":
                print("Column", column_number, "is full, choose another one!")
                break

            # If an empty space is available, enter the player's symbol in that space, print the grid and change the turn
            elif piece_list[a][column_number - 1] == "-":
                piece_list[a][column_number - 1] = turn_counter.player_symbol
                last_move.update_move_details(a, column_number - 1, turn_counter.player_symbol)
                print(last_move)
                turn_counter.change_turn()
                break

    # If a column is chosen that doesn't exist, print this error message
    else:
        print("That column doesn't exist. Please choose a column between 1 and 7.")     # TO DO: Make this the 'if', and the loop the 'else'

def check_vertical_victory():
    a = 0
    for b in range(last_move.row, grid_height - 1):
        if piece_list[b][last_move.column] == last_move.symbol:
            a +=1
        else:
            break
    
    if a == 4:
        return True
    else:
        return False

def check_horizontal_victory():
    a = 0
    for b in range(grid_width - 1):
        if piece_list[last_move.row][b] == last_move.symbol:
            a += 1
            if a == 4:
                break
        else:
            a = 0
    
    if a == 4:
        return True

    else:
        return False
    
# TO DO: Check for diagonal victories
def check_diagonal_victory_bottomleft_topright():
    a = 0
    b = last_move.row
    if last_move.row != 5 and last_move.column != 0:
        for c in range(last_move.column - 1, -1, -1):
            if b + 1 <= 5 and piece_list[b + 1][c] == last_move.symbol:
                a += 1
                b += 1
            else:
                break
    
    if last_move.row != 0 and last_move.column != 6:
        for d in range(last_move.column + 1, grid_width, 1):
            if b - 1 >= 0 and piece_list[b - 1][d] == last_move.symbol:
                a += 1
                b -= 1
            else:
                break

    if a >= 3:
        return True

def check_diagonal_victory_topleft_bottomright():
    a = 0
    b = last_move.row
    if last_move.row != 0 and last_move.column != 0:
        for c in range(last_move.column -1, -1, -1):
            if b - 1 >= 0 and piece_list[b - 1][c] == last_move.symbol:
                a += 1
                b -= 1
            else:
                break
    
    if last_move.row != 5 and last_move.column != 6:
        for d in range(last_move.column + 1, grid_width, 1):
            if b + 1 <= 5 and piece_list[b + 1][d] == last_move.symbol:
                a += 1
                b += 1
            else:
                break

    if a >= 3:
        return True

def check_diagonal_victory():
    if check_diagonal_victory_bottomleft_topright() == True or check_diagonal_victory_topleft_bottomright() == True:
        return True

def check_victory():
    if check_vertical_victory() == True or check_horizontal_victory() == True or check_diagonal_victory() == True:
        return True
    else:
        return False

def check_draw():
    if turn_counter.turn_number >= 43:
        return True
    else:
        return False

def check_game_end():
    if check_victory() == True or check_draw() == True:
        return True
    else:
        return False

game_finished = False

while game_finished == False:
    display_game()
    print(turn_counter)
    player_move(int(input("Column number: ")))
    print(check_victory())
    game_finished = check_game_end()

        
if game_finished == True:
    display_game()
    if check_victory() == True:
        print(f"Congratulations player {last_move.symbol}! You've won the game.")
    elif check_draw() == True:
        print(f"It's a draw! Well played to both players.")

# TO DO: Add a way or method to start the game again.


