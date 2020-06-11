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
from grid import (
    STARTING_GRID,
    insert_food_to_grid
)
from movement import (
    move,
    find_head_coord
)

GOOGLE_CLIENT = get_client()
WORKSHEET = get_worksheet(GOOGLE_CLIENT, 'SheetSnake', 'SheetSnake')


def snake():
    print('Starting SNAKE...')
    update_status(WORKSHEET, 'Starting new game...')
    time.sleep(5)

    print('Changing direction to a')
    update_direction(WORKSHEET, 'a')

    print('Updating grid for new game.')
    starting_grid_with_food = insert_food_to_grid(STARTING_GRID)
    update_grid_values(WORKSHEET, starting_grid_with_food)

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

    current_grid = deepcopy(starting_grid_with_food)
    head_history = [find_head_coord(current_grid)]
    length = 1
    alive = True

    print('Starting game while loop.')
    while(alive):
        current_direction = get_direction(WORKSHEET)

        move_data = move(current_direction, current_grid, head_history, length)
        new_grid = move_data['new_grid']
        head_history = move_data['head_history']
        length = move_data['length']
        alive = move_data['alive']
        reason = move_data['reason']

        update_grid_values(WORKSHEET, new_grid)
        current_grid = get_grid_values(WORKSHEET)

    update_status(WORKSHEET, reason)

    print('Updating grid for new game.')
    update_grid_values(WORKSHEET, STARTING_GRID)

    print('Finished while loop. Game over!')
