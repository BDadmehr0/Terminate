import time
import os
import sys
import keyboard

GAME_STATUS = True

# Map
def load_grid_from_file(file_path):
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]
    # Debug: Print the loaded grid
    for row in grid:
        print(''.join(row))
    return grid

def print_grid(grid):
    for row in grid:
        print(' '.join(row))

# Player
def place_player(grid, position):
    x, y = position
    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        grid[x][y] = 'P'
    else:
        raise ValueError("Player position is out of grid bounds.")

def move_player(position, direction, grid_size):
    x, y = position
    if direction == 'up' and x > 0:
        x -= 1
    elif direction == 'down' and x < grid_size - 1:
        x += 1
    elif direction == 'left' and y > 0:
        y -= 1
    elif direction == 'right' and y < grid_size - 1:
        y += 1
    return (x, y)

# System
def cs(): # clear screen
    time.sleep(0.2)
    os.system('clear')

def main():
    # Load map from file
    grid = load_grid_from_file('map.txt')
    grid_size = len(grid)
    
    # Initial player position
    player_position = (0, 0)

    while GAME_STATUS:
        cs()
        
        # Clear the grid and place the player
        grid = load_grid_from_file('map.txt')
        place_player(grid, player_position)
        
        # Print the grid with the player
        print_grid(grid)

        # Capture key presses
        if keyboard.is_pressed('w'):
            player_position = move_player(player_position, 'up', grid_size)
        elif keyboard.is_pressed('s'):
            player_position = move_player(player_position, 'down', grid_size)
        elif keyboard.is_pressed('a'):
            player_position = move_player(player_position, 'left', grid_size)
        elif keyboard.is_pressed('d'):
            player_position = move_player(player_position, 'right', grid_size)

if __name__ == "__main__":

    # Hide the cursor
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

    try:
        main()
    finally:
        # Show the cursor again
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()

