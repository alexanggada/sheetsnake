from copy import deepcopy
import time

from api import (
    get_client,
    get_direction,
    get_grid_values,
    get_worksheet,
    update_direction,
    update_grid_values,
    update_status
)
from food import insert_food_to_grid
from grid import STARTING_GRID
from movement import (
    move_head,
    find_head_coord
)
from rules import is_alive

GOOGLE_CLIENT = get_client()
WORKSHEET = get_worksheet(GOOGLE_CLIENT, 'SheetSnake', 'SheetSnake')


def snake():
    print('Starting SNAKE...')
    update_status(WORKSHEET, 'Starting new game...')
    time.sleep(5)

    print('Changing direction to l')
    update_direction(WORKSHEET, 'l')

    print('Updating grid for new game.')
    # starting_grid_with_food = insert_food_to_grid(STARTING_GRID)
    # update_grid_values(WORKSHEET, starting_grid_with_food)
    # current_grid = deepcopy(starting_grid_with_food)

    update_grid_values(WORKSHEET, STARTING_GRID)
    current_grid = deepcopy(STARTING_GRID)

    print('Starting countdown.')
    update_status(WORKSHEET, 'Starting in 3...')
    time.sleep(1)
    update_status(WORKSHEET, 'Starting in 2...')
    time.sleep(1)
    update_status(WORKSHEET, 'Starting in 1...')
    time.sleep(1)
    update_status(WORKSHEET, 'Start!')
    time.sleep(1)
    update_status(WORKSHEET, 'Playing')

    print('Starting game while loop.')
    # movement_history = []
    while(is_alive(current_grid)):
        current_direction = get_direction(WORKSHEET)
        # new_grid = move_head(current_direction, current_grid, movement_history)
        new_grid = move_head(current_direction, current_grid)
        # movement_history = [find_head_coord(current_grid)] + movement_history
        update_grid_values(WORKSHEET, new_grid)
        current_grid = get_grid_values(WORKSHEET)

    update_status(WORKSHEET, 'GAME OVER!')

    print('Updating grid for new game.')
    update_grid_values(WORKSHEET, STARTING_GRID)

    print('Finished while loop. Game over!')
