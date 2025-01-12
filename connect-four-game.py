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



# player_move let's the player put their move in
def player_move(column_number):

    # First, check if a column_number is given that fits on the board
    if 1 <= column_number <= grid_width:

        # Then, go backwards through the following range and look for the first empty space in the selected column
        for a in range(grid_height - 1, -1, -1):

            # If no empty space is found, print a message that the column is full
            if piece_list[0][column_number - 1] != "-":
                display_game()
                print("Column", column_number, "is full, choose another one!")
                break

            # If an empty space is available, enter the player's symbol in that space, print the grid and change the turn
            elif piece_list[a][column_number - 1] == "-":
                piece_list[a][column_number - 1] = turn_counter.player_symbol
                display_game()
                turn_counter.change_turn()
                print(turn_counter)
                break

    # If a column is chosen that doesn't exist, print this error message
    else:
        print("That column doesn't exist. Please choose a column between 1 and 7.")

game_finished = False

while game_finished == False:
    display_game()
    print(turn_counter)
    player_move(int(input("Column number: ")))
    # Here a break definition should be added, stopping the game when there's a winner, or no more spaces are left.
    # for example:
    # game_finished = check_victory()

def check_vertical_victory():
    pass