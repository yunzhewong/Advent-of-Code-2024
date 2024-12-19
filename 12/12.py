import os
import sys
import time
from enum import Enum
from typing import Callable, Dict, List, Tuple

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.operate_on_lines import operate_on_lines, operate_on_test


def parse_grid():
    grid = []

    def fn(l):
        grid.append(list(l))

    operate_on_lines(fn)

    return grid


DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def in_grid(grid, position):
    height = len(grid)
    width = len(grid[0])
    return (
        position[0] >= 0
        and position[0] < height
        and position[1] >= 0
        and position[1] < width
    )


def search(position, nodeFn, searchFn):
    nodeFn(position)
    for direction in DIRECTIONS:
        next_position = (position[0] + direction[0], position[1] + direction[1])

        if not searchFn(next_position):
            continue

        search(next_position, nodeFn, searchFn)


def search_for_region(grid, position):
    same_region = []
    start_char = grid[position[0]][position[1]]

    def nodeFn(current_position):
        same_region.append(current_position)

    def continueFn(next_position):
        if next_position in same_region:
            return False

        if not in_grid(grid, next_position):
            return False

        next_char = grid[next_position[0]][next_position[1]]

        if next_char != start_char:
            return False

        return True

    search(position, nodeFn, continueFn)
    return same_region


def identify_regions(grid):
    regions = []
    encountered = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            position = (i, j)
            if position in encountered:
                continue

            same_region = search_for_region(grid, position)
            encountered += same_region

            regions.append(same_region)

    return regions


def search_perimeter_length(grid, region):
    perimeter_positions = []

    def nodeFn(current_position):
        pass

    def searchFn(next_position):
        if next_position in region:
            return False

        perimeter_positions.append(next_position)

        return False

    for position in region:
        search(position, nodeFn, searchFn)

    return len(perimeter_positions)


def compute_cost(grid, region):
    i, j = region[0]

    area = len(region)
    perimeter = search_perimeter_length(grid, region)

    return area * perimeter


def twelve_a():
    grid = parse_grid()
    regions = identify_regions(grid)
    total = 0
    for region in regions:
        total += compute_cost(grid, region)
    print(total)


if __name__ == "__main__":
    twelve_a()
