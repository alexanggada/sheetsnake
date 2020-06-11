from copy import deepcopy


def move(direction, last_grid, head_history, length):
    try:
        initial_head_row, initial_head_col = find_head_coord(last_grid)
    except:
        # Dying by self-eating
        print('Death by self-eating!')
        return {
            'new_grid': last_grid,
            'head_history': head_history,
            'length': length,
            'alive': False,
            'reason': 'Death by self-eating!'
        }

    if direction == 'w':
        next_head_coord = [(initial_head_row - 1, initial_head_col)]
        head_history = next_head_coord + head_history
    elif direction == 'a':
        next_head_coord = [(initial_head_row, initial_head_col - 1)]
        head_history = next_head_coord + head_history
    elif direction == 's':
        next_head_coord = [(initial_head_row + 1, initial_head_col)]
        head_history = next_head_coord + head_history
    elif direction == 'd':
        next_head_coord = [(initial_head_row, initial_head_col + 1)]
        head_history = next_head_coord + head_history
    else:
        return last_grid

    return moving(last_grid, head_history, length)


def moving(last_grid, head_history, length):
    next_row, next_col = head_history[0]
    next_val = last_grid[next_row][next_col]

    new_grid = deepcopy(last_grid)

    # Dying by grid bounds
    grid_bounds = [0, 11]
    if next_row in grid_bounds or next_col in grid_bounds:
        print('Death by grid!')
        return {
            'new_grid': new_grid,
            'head_history': head_history,
            'length': length,
            'alive': False,
            'reason': 'Death by out-of-bounds!'
        }
    
    # Eating
    if next_val == 'f':
        length = length + 1

    # Making the body
    new_grid[next_row][next_col] = 'h'
    for body_row, body_col in head_history[1:length]:
        new_grid[body_row][body_col] = 'b'

    # Making the empty space
    for empty_row, empty_col in head_history[length:]:
        new_grid[empty_row][empty_col] = ''

    return {
        'new_grid': new_grid,
        'head_history': head_history,
        'length': length,
        'alive': True,
        'reason': ''
    }


def find_head_coord(grid):
    for row_coord, row in enumerate(grid):
        for col_coord, value in enumerate(row):
            if value == 'h':
                return (row_coord, col_coord)
