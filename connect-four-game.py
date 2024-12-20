# The piece_list keeps track of which pieces have been placed
piece_list = [["-","-","-","-","-","-","-"],
              ["-","-","-","-","-","-","-"],
              ["-","-","-","-","-","-","-"],
              ["-","-","-","-","-","-","-"],
              ["-","-","-","-","-","-","-"],
              ["-","-","-","-","-","-","-"]]

grid_width = 7
grid_height = 6

# The function display_game prints the grid with a size determined by grid_width and grid_height
# Inside the grid, the appropriate value from piece_list is printed
def display_game():
    c = 65

    # First row
    print(f"  ", end='')
    for j in range(grid_width):
        print(f"| {j+1} ", end='')
    print("| ")
    print((grid_width*4+4)*"-")

    # Other rows
    for i in range(grid_height):
        print(f"{chr(c+i)} ", end='')
        for j in range(grid_width):
            print(f"| {piece_list[i][j]} ", end='')
        print("| ")
        print((grid_width*4+4)*"-")


display_game()

# player_move let's the player put their move in
# Through player_symbol, the player can select the symbol they are playing with
# Through column_number, the player selects in which column to play the piece
def player_move(current_player_symbol, column_number):
    for a in range(6):
        if piece_list[a][column_number-1] == "-":
            piece_list[a][column_number-1] = current_player_symbol
            
            # Currently, this code is not functional. Need to make it work so player doesn't have to input the symbol
            # if current_player_symbol == "X":
            #    current_player_symbol = "O"
            # else: current_player_symbol = "X" 
            break
        
        elif piece_list[grid_height-1][column_number-1] != "-":
                print("")
                print("That column is full, choose another one!")
                print("")
                break
    
    # This part is also not functional yet. Need to make it work so player doesn't have to input the symbol
    # print("It's player ", current_player_symbol, "'s turn")
    display_game()