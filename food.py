from copy import deepcopy
from random import randrange


def insert_food_to_grid(grid_with_snake):
    new_grid = deepcopy(grid_with_snake)
    rand_row = randrange(1, 10)
    rand_col = randrange(1, 10)
    new_grid[rand_row][rand_col] = 'f'
    return new_grid
