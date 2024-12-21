import math
import os
import sys
import time
from enum import Enum
from typing import Callable, Dict, List, Tuple

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.operate_on_lines import operate_on_lines, operate_on_test

# BOARD_SIZE = (11, 7)
BOARD_SIZE = (101, 103)


def parse_xy(string):
    equals = string.find("=")
    comma = string.find(",")
    x = int(string[equals + 1 : comma])
    y = int(string[comma + 1 :])
    return (x, y)


def parse_robots():
    robots = []

    def fn(l: str):
        sections = l.split(" ")
        pos = parse_xy(sections[0])
        vel = parse_xy(sections[1])
        robots.append((pos, vel))

    operate_on_lines(fn)

    return robots


def compute_raw_position(robot, iterations):
    pos = robot[0]
    vel = robot[1]
    return (pos[0] + iterations * vel[0], pos[1] + iterations * vel[1])


def wrap(value, max_size):
    if value > 0:
        return value % max_size

    offset = math.ceil((-1 * value) / max_size) * max_size
    value += offset
    return value % max_size


def wrap_position(raw_position):
    x = wrap(raw_position[0], BOARD_SIZE[0])
    y = wrap(raw_position[1], BOARD_SIZE[1])
    return x, y


def count_quadrant(state, topLeft, size):
    lowX, lowY = topLeft
    width, height = size

    total = 0
    for i in range(lowY, lowY + height):
        for j in range(lowX, lowX + width):
            total += state[i][j]
    return total


def get_safety_factor(state):
    quadrant_width = int((BOARD_SIZE[0] - 1) / 2)
    quadrant_height = int((BOARD_SIZE[1] - 1) / 2)
    quadrant_size = quadrant_width, quadrant_height
    half_width = int((BOARD_SIZE[0] + 1) / 2)
    half_height = int((BOARD_SIZE[1] + 1) / 2)

    product = 1
    product *= count_quadrant(state, (0, 0), quadrant_size)
    product *= count_quadrant(state, (half_width, 0), quadrant_size)
    product *= count_quadrant(state, (0, half_height), quadrant_size)
    product *= count_quadrant(state, (half_width, half_height), quadrant_size)
    print(product)


def fourteen_a():
    robots = parse_robots()

    state = [[0 for _ in range(BOARD_SIZE[0])] for _ in range(BOARD_SIZE[1])]

    for robot in robots:
        raw_position = compute_raw_position(robot, 100)
        i, j = wrap_position(raw_position)
        state[j][i] += 1

    get_safety_factor(state)


if __name__ == "__main__":
    fourteen_a()
