import os
import sys
import time
from enum import Enum
from typing import Callable, Dict, List, Tuple

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.operate_on_lines import operate_on_lines, operate_on_test


def parse_map():
    map = []

    def fn(l):
        map.append([int(i) for i in list(l)])

    operate_on_lines(fn)
    return map


def find_heads(map):
    heads = []

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                heads.append((i, j))

    return heads


def in_map(map, position):
    height = len(map)
    width = len(map[0])

    return (
        position[0] >= 0
        and position[0] < height
        and position[1] >= 0
        and position[1] < width
    )


DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def found_nine_positions(position, map):
    i, j = position
    current_height = map[i][j]

    if current_height == 9:
        return [position]

    positions = []
    for direction in DIRECTIONS:
        next_position = (position[0] + direction[0], position[1] + direction[1])

        if not in_map(map, next_position):
            continue

        next_i, next_j = next_position
        next_height = map[next_i][next_j]

        if next_height != current_height + 1:
            continue

        new_positions = found_nine_positions(next_position, map)

        for new_position in new_positions:
            if new_position in positions:
                continue

            positions.append(new_position)

    return positions


def ten_a():
    map = parse_map()
    heads = find_heads(map)

    total = 0
    for head in heads:
        res = found_nine_positions(head, map)
        total += len(res)

    print(total)


def found_nine_count(position, map):
    i, j = position
    current_height = map[i][j]

    if current_height == 9:
        return 1

    total = 0
    for direction in DIRECTIONS:
        next_position = (position[0] + direction[0], position[1] + direction[1])

        if not in_map(map, next_position):
            continue

        next_i, next_j = next_position
        next_height = map[next_i][next_j]

        if next_height != current_height + 1:
            continue

        total += found_nine_count(next_position, map)

    return total


def ten_b():
    map = parse_map()
    heads = find_heads(map)

    total = 0
    for head in heads:
        res = found_nine_count(head, map)
        total += res

    print(total)


if __name__ == "__main__":
    ten_b()
