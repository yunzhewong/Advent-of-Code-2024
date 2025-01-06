import math
import os
import sys
import time
from enum import Enum
from typing import Any, Callable, Dict, List, Tuple

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


def shift_robot(robot_pos, movement, map):
    map[robot_pos[0]][robot_pos[1]] = "."

    next_robot_pos = move_from_pos(robot_pos, movement)
    map[next_robot_pos[0]][next_robot_pos[1]] = "@"

    return next_robot_pos


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

    next_robot_pos = shift_robot(robot_pos, move, map)
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


def expand_map(map):
    expanded = []
    for line in map:
        expanded_line = []
        for char in line:
            if char == "#":
                expanded_line.append("#")
                expanded_line.append("#")
            if char == "O":
                expanded_line.append("[")
                expanded_line.append("]")
            if char == ".":
                expanded_line.append(".")
                expanded_line.append(".")
            if char == "@":
                expanded_line.append("@")
                expanded_line.append(".")
        expanded.append(expanded_line)
    return expanded


def get_box_positions(map, tip_pos):
    tip_char = map[tip_pos[0]][tip_pos[1]]

    if tip_char == "]":
        return [move_from_pos(tip_pos, (0, -1)), tip_pos]
    return [tip_pos, move_from_pos(tip_pos, (0, 1))]


def order_boxes(box_positions: List[Any], movement):
    if movement[1] == -1:
        return box_positions[::-1]
    return box_positions


def get_next_tips(box_positions, movement):
    if movement[0] != 0:
        return [move_from_pos(pos, movement) for pos in box_positions]

    if movement[1] == 1:
        return [move_from_pos(box_positions[1], movement)]
    return [move_from_pos(box_positions[0], movement)]


def move_robot_b(robot_pos, movement, map):
    next_pos = move_from_pos(robot_pos, movement)

    boxes_to_move = []
    search_tip_positions = [next_pos]

    while len(search_tip_positions) > 0:
        next_tips = []
        for tip_pos in search_tip_positions:
            tip_char = map[tip_pos[0]][tip_pos[1]]
            if tip_char == "#":
                return robot_pos

            if tip_char == ".":
                continue

            box_positions = get_box_positions(map, tip_pos)
            next_tips += get_next_tips(box_positions, movement)
            boxes_to_move += order_boxes(box_positions, movement)
        search_tip_positions = next_tips

    moved_boxes = []

    for i in range(len(boxes_to_move)):
        old_position = boxes_to_move[len(boxes_to_move) - i - 1]
        if old_position in moved_boxes:
            continue
        char = map[old_position[0]][old_position[1]]
        map[old_position[0]][old_position[1]] = "."
        new_position = move_from_pos(old_position, movement)
        map[new_position[0]][new_position[1]] = char
        moved_boxes.append(old_position)

    next_robot_pos = shift_robot(robot_pos, movement, map)
    return next_robot_pos


def sum_box_coords_b(map):

    total = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "[":
                total += 100 * i + j
    return total


def fifteen_b():
    map, movements = read_input()
    map = expand_map(map)
    pretty_print(map)

    robot_pos = find_robot_position(map)

    if robot_pos is None:
        raise Exception("Not Possible")

    for char_move in movements:
        movement = read_move(char_move)
        robot_pos = move_robot_b(robot_pos, movement, map)

    pretty_print(map)
    print(sum_box_coords_b(map))


if __name__ == "__main__":
    fifteen_b()
