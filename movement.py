from copy import deepcopy


# def move_head(direction, last_grid, movement_history, size):
def move_head(direction, last_grid):
    initial_row, initial_col = find_head_coord(last_grid)

    if direction == 'u':
        next_row = initial_row - 1
        next_col = initial_col
        # if next_val == 'f':
            # return eating(initial_row, initial_col, next_row, next_col, last_grid)
    elif direction == 'd':
        next_row = initial_row + 1
        next_col = initial_col
        # if next_val == 'f':
        #     return eating(initial_row, initial_col, next_row, next_col, last_grid)
    elif direction == 'l':
        next_row = initial_row
        next_col = initial_col - 1
        # if next_val == 'f':
        #     return eating(initial_row, initial_col, next_row, next_col, last_grid)
    elif direction == 'r':
        next_row = initial_row
        next_col = initial_col + 1
        # if next_val == 'f':
        #     return eating(initial_row, initial_col, next_row, next_col, last_grid)
    else:
        return last_grid

    new_grid = deepcopy(last_grid)
    new_grid[initial_row][initial_col] = ''
    new_grid[next_row][next_col] = 'S'
    return new_grid


# def eating(last_size, next_row, next_col, last_grid, movement_history):
#     new_grid = deepcopy(last_grid)
#     for i in movement_history[:last_size:
#         new_grid
#     new_grid[initial_row][initial_col] = 's'
#     new_grid[next_row][next_col] = 'S'
#     return new_grid, new_size



def find_head_coord(grid):
    for row_coord, row in enumerate(grid):
        for col_coord, value in enumerate(row):
            if value == 'S':
                return (row_coord, col_coord)
