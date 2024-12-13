import sys
import os
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


def six_a():
    map = parse_map()
    i, j = parse_start(map)
    direction = (-1, 0)

    height = len(map)
    width = len(map[0])

    while True:
        map[i][j] = "X"
        next_i = i + direction[0]
        next_j = j + direction[1]

        if next_i >= height or next_i < 0:
            break

        if next_j >= width or next_j < 0:
            break

        next_char = map[next_i][next_j]

        if next_char == "#":
            direction = get_next_direction(direction)
        else:
            i = next_i
            j = next_j

    total = 0
    for line in map:
        for char in line:
            if char == "X":
                total += 1

    print(total)


if __name__ == "__main__":
    six_a()
