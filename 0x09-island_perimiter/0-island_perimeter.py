#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """ Returns the perimeter of the island described in grid.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                cell_perimeter = 4

                if i > 0 and grid[i - 1][j] == 1:
                    cell_perimeter -= 1

                if i < rows - 1 and grid[i + 1][j] == 1:
                    cell_perimeter -= 1

                if j > 0 and grid[i][j - 1] == 1:
                    cell_perimeter -= 1

                if j < cols - 1 and grid[i][j + 1] == 1:
                    cell_perimeter -= 1

                perimeter += cell_perimeter

    return perimeter
