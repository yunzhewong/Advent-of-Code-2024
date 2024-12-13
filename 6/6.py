import sys
import os
import time
from typing import Callable, Dict, List, Tuple

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.operate_on_lines import operate_on_lines, operate_on_test


def parse_map():
    map = []

    def add_to_map(line: str):
        map.append(list(line))

    operate_on_lines(add_to_map)

    return map


def parse_start(map: List[List[str]]):
    for i in range(len(map)):
        for j in range(len(map[i])):
            char = map[i][j]

            if char != "^":
                continue

            return i, j


def get_next_direction(direction: Tuple[int, int]):
    if direction == (-1, 0):  # UP
        return (0, 1)
    if direction == (0, 1):  # RIGHT
        return (1, 0)
    if direction == (1, 0):  # DOWN
        return (0, -1)
    if direction == (0, -1):  # LEFT
        return (-1, 0)


def within_map(i, j, height, width):
    if i >= height or i < 0:
        return False
    if j >= width or j < 0:
        return False
    return True


def next_pos(current_pos, direction):
    next_i = current_pos[0] + direction[0]
    next_j = current_pos[1] + direction[1]
    return next_i, next_j


def next_state(map, current_pos, next_pos, direction):
    i, j = current_pos
    next_i, next_j = next_pos
    next_char = map[next_i][next_j]

    if next_char == "#":
        return (i, j), get_next_direction(direction)
    return (next_i, next_j), direction


def six_a():
    map = parse_map()
    i, j = parse_start(map)
    direction = (-1, 0)

    height = len(map)
    width = len(map[0])

    while True:
        map[i][j] = "X"
        next_i, next_j = next_pos((i, j), direction)

        if not within_map(next_i, next_j, height, width):
            break

        (i, j), direction = next_state(map, (i, j), (next_i, next_j), direction)

    total = 0
    for line in map:
        for char in line:
            if char == "X":
                total += 1
    print(total)


def six_b():
    history = {}
    history[(1, 0)] = 5
    print(history.keys())


if __name__ == "__main__":
    six_a()
