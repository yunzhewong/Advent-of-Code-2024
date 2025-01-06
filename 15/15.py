import math
import os
import sys
import time
from enum import Enum
from typing import Callable, Dict, List, Tuple

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.operate_on_lines import operate_on_lines, operate_on_test


def read_move(move: str):
    if move == "^":
        return (-1, 0)
    if move == ">":
        return (0, 1)
    if move == "v":
        return (1, 0)
    if move == "<":
        return (0, -1)
    raise Exception("Not possible")


def read_input():
    map = []
    movements = []

    state = [False]

    def fn(l):
        if l == "":
            state[0] = True
            return

        if not state[0]:
            map.append(list(l))
        else:
            for char in l:
                movements.append(char)

    operate_on_lines(fn)

    return map, movements


def find_robot_position(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "@":
                return i, j

    return None


def move_from_pos(pos, move):
    return (pos[0] + move[0], pos[1] + move[1])


def move_robot(robot_pos, move, map):
    next_pos = move_from_pos(robot_pos, move)

    boxes_positions = []

    while True:
        next_char = map[next_pos[0]][next_pos[1]]
        if next_char == "#":
            return robot_pos

        if next_char == ".":
            break

        boxes_positions.append(next_pos)
        next_pos = move_from_pos(next_pos, move)

    for position in boxes_positions:
        new_position = move_from_pos(position, move)
        map[new_position[0]][new_position[1]] = "O"

    map[robot_pos[0]][robot_pos[1]] = "."

    next_robot_pos = move_from_pos(robot_pos, move)
    map[next_robot_pos[0]][next_robot_pos[1]] = "@"

    return next_robot_pos


def pretty_print(map):
    for row in map:
        print("".join(row))


def sum_of_box_positions(map):
    total = 0

    for i in range(len(map)):
        for j in range(len(map[i])):

            if map[i][j] == "O":
                total += 100 * i + j

    return total


def fifteen_a():
    map, movements = read_input()
    robot_pos = find_robot_position(map)

    if robot_pos is None:
        raise Exception("Not Possible")

    for char_move in movements:
        movement = read_move(char_move)
        robot_pos = move_robot(robot_pos, movement, map)

    pretty_print(map)
    print(robot_pos)

    print(sum_of_box_positions(map))


if __name__ == "__main__":
    fifteen_a()
