# The piece_list keeps track of which pieces have been placed
piece_list = [["-","-","-","-","-","-","-"],
              ["-","-","-","-","-","-","-"],
              ["-","-","-","-","-","-","-"],
              ["-","-","-","-","-","-","-"],
              ["-","-","-","-","-","-","-"],
              ["-","-","-","-","-","-","-"]]

print(piece_list)

def display_game(grid_width, grid_height):
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


display_game(7, 6)

