import random, time, copy

# Define the width and height of the grid.
WIDTH = 60
HEIGHT = 10

# Initialize a grid for the cells, represented as a list of lists.
nextCells = []
for x in range(WIDTH):
    column = [] # Initialize a new column.
    for y in range(HEIGHT):
        # Randomly assign each cell as either alive ('#') or dead (' ').
        if random.randint(0, 1) == 0:
            column.append('#') # Cell is alive.
        else:
            column.append(' ') # Cell is dead.
    nextCells.append(column) # Add the column to the grid.

# Start the main loop of the game.
while True:
    print('\n\n\n\n\n') # Print newlines to create a visual separation between steps.
    currentCells = copy.deepcopy(nextCells) # Create a deep copy of the cells for the current generation.

    # Display the current state of the cells on the screen.
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # Print the current cell state without a newline.
        print() # End the current row of cells with a newline.

    # Calculate the next generation of cells based on the current state.
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Calculate the coordinates of neighboring cells with wrap-around.
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count the number of living neighbors.
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-right neighbor is alive.
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # Left neighbor is alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbors    += 1 # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-right neighbor is alive.

            # Apply Conway's Game of Life rules to determine the next state of each cell.
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # A living cell with 2 or 3 living neighbors stays alive.
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # A dead cell with exactly 3 living neighbors becomes alive.
                nextCells[x][y] = '#'
            else:
                # Any other cell becomes dead or stays dead.
                nextCells[x][y] = ' '

    time.sleep(1) # Pause for 1 second to make the evolution visible.
