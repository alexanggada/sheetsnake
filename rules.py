from movement import find_head_coord


def is_alive(current_grid):
    current_row, current_col = find_head_coord(current_grid)
    dying_coords = [0, 11]
    if current_row in dying_coords or current_col in dying_coords:
        return False
    else:
        return True
