from copy import deepcopy
from random import randrange

EMPTY_GRID = [
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', '',  '',  '',  '',  '',  '',  '',  '',  '',  '', 'o'],
    ['o', '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  'o'],
    ['o', '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  'o'],
    ['o', '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  'o'],
    ['o', '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  'o'],
    ['o', '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  'o'],
    ['o', '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  'o'],
    ['o', '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  'o'],
    ['o', '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  'o'],
    ['o', '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
]


def insert_starting_head_and_food(empty_grid):
    new_grid = deepcopy(empty_grid)

    head_row, head_col = get_random_empty_cell_coord(new_grid)
    new_grid[head_row][head_col] = 'h'

    food_row, food_col = get_random_empty_cell_coord(new_grid)
    new_grid[food_row][food_col] = 'f'
    return new_grid


def insert_food_to_grid(last_grid):
    new_grid = deepcopy(last_grid)
    food_row, food_col = get_random_empty_cell_coord(new_grid)
    new_grid[food_row][food_col] = 'f'
    return new_grid


def get_random_empty_cell_coord(last_grid):
    rand_row = randrange(1, 10)
    rand_col = randrange(1, 10)
    rand_val = last_grid[rand_row][rand_col]
    while rand_val != '':
        rand_row = randrange(1, 10)
        rand_col = randrange(1, 10)
        rand_val = last_grid[rand_row][rand_col]
    return rand_row, rand_col
