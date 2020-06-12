import time

from api import (
    get_client,
    get_direction,
    get_worksheet,
    update_grid_values,
    update_score,
    update_status
)
from grid import (
    EMPTY_GRID,
    insert_food_to_grid,
    insert_starting_head_and_food
)
from movement import (
    move,
    find_head_coord
)

GOOGLE_CLIENT = get_client()
WORKSHEET = get_worksheet(GOOGLE_CLIENT, 'SheetSnake', 'Arcade_Theme')


def snake():
    print('Starting SheetSnake...')
    update_status(WORKSHEET, 'Starting game')

    print('Updating grid for new game.')
    current_grid = insert_starting_head_and_food(EMPTY_GRID)
    update_grid_values(WORKSHEET, current_grid)
    head_history = [find_head_coord(current_grid)]
    length = 1
    alive = True

    print('Resetting score to 0')
    update_score(WORKSHEET, 0)

    time.sleep(3)
    countdown(WORKSHEET)

    print('Starting game while loop.')
    while(alive):
        current_direction = get_direction(WORKSHEET)

        old_length = length
        move_data = move(current_direction, current_grid, head_history, length)
        head_history = move_data['head_history']
        length = move_data['length']
        alive = move_data['alive']

        if length > old_length:
            print('Inserted food')
            current_grid = insert_food_to_grid(move_data['new_grid'])
        else:
            current_grid = move_data['new_grid']

        update_grid_values(WORKSHEET, current_grid)
        time.sleep(1)
        update_score(WORKSHEET, length - 1)

    update_status(WORKSHEET, 'Game Over!')
    print('Finished while loop. Game over!')


def countdown(WORKSHEET):
    print('Starting countdown.')
    update_status(WORKSHEET, 'Starting in 3')
    time.sleep(1)
    update_status(WORKSHEET, 'Starting in 2')
    time.sleep(1)
    update_status(WORKSHEET, 'Starting in 1')
    time.sleep(1)
    update_status(WORKSHEET, 'Start!')
    time.sleep(1)
    update_status(WORKSHEET, 'Playing')


def debug(head_history, length, current_grid):
    from pprint import pprint

    print(head_history)
    print(length)
    print('New grid:')
    pprint(current_grid)
    print('\n')
