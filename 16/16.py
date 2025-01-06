import math
import os
import sys
import time
from enum import Enum
from typing import Callable, Dict, List, Tuple

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.operate_on_lines import operate_on_lines, operate_on_test


def read_maze():
    maze = []

    def fn(l):
        maze.append(list(l))

    operate_on_lines(fn)

    return maze


def move(position, direction):
    return (position[0] + direction[0], position[1] + direction[1])


def rotate_counterclockwise(direction):
    return (direction[1], -direction[0])


def rotate_clockwise(direction):
    return (-direction[1], direction[0])


def find_start(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "S":
                return (i, j)
    raise Exception("Start Expected")


def is_wall(maze, position):
    return maze[position[0]][position[1]] == "#"


def sixteen_a():
    maze = read_maze()

    def sortkey(obj):
        return obj[0]

    start_pos = find_start(maze)

    visited = []
    queue = [(0, start_pos, (0, 1))]
    while True:
        if len(queue) == 0:
            break

        (score, position, direction) = queue.pop(0)
        if position in visited:
            continue
        visited.append(position)

        if maze[position[0]][position[1]] == "E":
            print(score, position, direction)
            break

        next_pos = move(position, direction)
        if not is_wall(maze, next_pos):
            queue.append((score + 1, next_pos, direction))

        clockwise_dir = rotate_clockwise(direction)
        clockwise_pos = move(position, clockwise_dir)
        if not is_wall(maze, clockwise_pos):
            queue.append((score + 1001, clockwise_pos, clockwise_dir))

        counterclockwise_dir = rotate_counterclockwise(direction)
        counterclockwise_pos = move(position, counterclockwise_dir)
        if not is_wall(maze, counterclockwise_pos):
            queue.append((score + 1001, counterclockwise_pos, counterclockwise_dir))

        queue.sort(key=sortkey)


if __name__ == "__main__":
    sixteen_a()
