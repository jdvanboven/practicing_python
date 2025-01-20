class Dimensions:
    def __init__(self):
        self.width = 7
        self.height = 6

    def __str__(self):
        return f"The game grid is {self.width} columns wide and {self.height} rows high"

    # change_turn is a method to increase turn number and change player after every turn

gamegrid = Dimensions()

gamegrid.width = 7
gamegrid.height = 6

piece_list = [["-"] * gamegrid.width for i in range(gamegrid.height)]

def display_game():
    c = 65

    # First row
    print("")
    print(f"  ", end="")
    for j in range(gamegrid.width):
        print(f"| {j+1} ", end="")
    print("| ")
    print((gamegrid.width * 4 + 4) * "-")

    # Other rows
    for i in range(gamegrid.height):
        print(f"{chr(c+i)} ", end="")
        for j in range(gamegrid.width):
            print(f"| {piece_list[i][j]} ", end="")
        print("| ")
        print((gamegrid.width * 4 + 4) * "-")

class Counter:
    def __init__(self):
        self.number = 1 
        self.player_symbol = "X"

    def __str__(self):
        return f"It's turn {self.number}. Player {self.player_symbol}, your move!"

    # change_turn is a method to increase turn number and change player after every turn
    def change_turn(self):
        self.number += 1
        if self.player_symbol == "X":
            self.player_symbol = "O"
        else:
            self.player_symbol = "X"

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

    if 1 <= column_number <= gamegrid.width:

        for a in range(gamegrid.height - 1, -1, -1):

            if piece_list[0][column_number - 1] != "-":
                print("Column", column_number, "is full, choose another one!")
                break

            elif piece_list[a][column_number - 1] == "-":
                piece_list[a][column_number - 1] = turn_counter.player_symbol
                last_move.update_move_details(a, column_number - 1, turn_counter.player_symbol)
                turn_counter.change_turn()
                break

# TO DO: Make this the 'if', and the loop the 'else'
    else:
        print("That column doesn't exist. Please choose a column between 1 and 7.")     

# Victory checks are not completely optimised for different size grids. This needs to be updated.
def check_vertical_victory():
    a = 0
    for b in range(last_move.row, gamegrid.height):
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
    for b in range(gamegrid.width - 1):
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
    
def check_diagonal_victory_bottomleft():
    a = 0
    b = last_move.row
    if last_move.row != 5 and last_move.column != 0:
        for c in range(last_move.column - 1, -1, -1):
            if b + 1 <= 5 and piece_list[b + 1][c] == last_move.symbol:
                a += 1
                b += 1
            else:
                break
    return a

def check_diagonal_victory_topright():
    a = 0
    b = last_move.row
    if last_move.row != 0 and last_move.column != 6:
        for d in range(last_move.column + 1, gamegrid.width, 1):
            if b - 1 >= 0 and piece_list[b - 1][d] == last_move.symbol:
                a += 1
                b -= 1
            else:
                break
    return a

def check_diagonal_victory_bottomleft_topright():
    if check_diagonal_victory_bottomleft() + check_diagonal_victory_topright() >= 3:
        return True

def check_diagonal_victory_topleft():
    a = 0
    b = last_move.row
    if last_move.row != 0 and last_move.column != 0:
        for c in range(last_move.column -1, -1, -1):
            if b - 1 >= 0 and piece_list[b - 1][c] == last_move.symbol:
                a += 1
                b -= 1
            else:
                break
    return a

def check_diagonal_victory_bottomright():
    a = 0
    b = last_move.row
    if last_move.row != 5 and last_move.column != 6:
            for d in range(last_move.column + 1, gamegrid.width, 1):
                if b + 1 <= 5 and piece_list[b + 1][d] == last_move.symbol:
                    a += 1
                    b += 1
                else:
                    break
    return a

def check_diagonal_victory_topleft_bottomright():
    if check_diagonal_victory_topleft() + check_diagonal_victory_bottomright() >= 3:
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
    if turn_counter.number >= 43:
        return True
    else:
        return False

def check_game_end():
    if check_victory() == True or check_draw() == True:
        return True
    else:
        return False

def restart_game(bool):
    pass

game_finished = False

while game_finished == False:
    display_game()
    print(turn_counter)
    player_move(int(input("Column number: ")))
    game_finished = check_game_end()

        
if game_finished == True:
    display_game()
    if check_victory() == True:
        print(f"Congratulations player {last_move.symbol}! You've won the game in {turn_counter.number - 1} turns.")
    elif check_draw() == True:
        print(f"It's a draw! Well played to both players.")
    restart_game(bool(input("Want to play again? True/False: ")))




# TO DO: Add a way or method to start the game again.


