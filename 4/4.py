import sys
import os
from typing import Callable, List, Tuple

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.operate_on_lines import operate_on_lines


def move_vertical(direction: int):
    return direction, 0


def move_horizontal(direction: int):
    return 0, direction


def move_diagonal_1(direction: int):
    return direction, direction


def move_diagonal_2(direction: int):
    return direction, -direction


def get_string_grid(string_grid: List[List[str]], i: int, j: int):
    if i >= len(string_grid) or i < 0:
        return ""
    if j >= len(string_grid[0]) or j < 0:
        return ""
    return string_grid[i][j]


def is_xmas(
    string_grid: List[List[str]], i: int, j: int, fn: Callable[[], Tuple[int, int]]
):
    v, h = fn()

    if get_string_grid(string_grid, i, j) != "X":
        return False
    if get_string_grid(string_grid, i + v, j + h) != "M":
        return False
    if get_string_grid(string_grid, i + 2 * v, j + 2 * h) != "A":
        return False
    if get_string_grid(string_grid, i + 3 * v, j + 3 * h) != "S":
        return False
    return True


def four_a():
    string_grid = []

    def fn(line: str):
        string_grid.append(line)

    operate_on_lines(fn)

    height = len(string_grid)
    width = len(string_grid[0])

    total = 0

    for i in range(height):
        for j in range(width):
            char = string_grid[i][j]

            if char != "X":
                continue

            if is_xmas(string_grid, i, j, lambda: move_vertical(1)):
                total += 1
            if is_xmas(string_grid, i, j, lambda: move_vertical(-1)):
                total += 1
            if is_xmas(string_grid, i, j, lambda: move_horizontal(1)):
                total += 1
            if is_xmas(string_grid, i, j, lambda: move_horizontal(-1)):
                total += 1
            if is_xmas(string_grid, i, j, lambda: move_diagonal_1(1)):
                total += 1
            if is_xmas(string_grid, i, j, lambda: move_diagonal_1(-1)):
                total += 1
            if is_xmas(string_grid, i, j, lambda: move_diagonal_2(1)):
                total += 1
            if is_xmas(string_grid, i, j, lambda: move_diagonal_2(-1)):
                total += 1

    print(total)


if __name__ == "__main__":
    four_a()
