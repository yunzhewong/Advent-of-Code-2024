import os
import sys
import time
from enum import Enum
from typing import Callable, Dict, List, Tuple

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.operate_on_lines import operate_on_lines, operate_on_test


def get_initial_stones():
    line = [""]

    def fn(l):
        line[0] = l

    operate_on_lines(fn)

    return [int(i) for i in line[0].split(" ")]


def blink_stone(stone):
    if stone == 0:
        return [1]

    string = str(stone)
    if len(string) % 2 == 0:
        half = int(len(string) / 2)
        return [int(string[:half]), int(string[half:])]

    return [2024 * stone]


def blink_stones(stones):
    output = []
    for stone in stones:
        output += blink_stone(stone)
    return output


def eleven_a():
    stones = get_initial_stones()
    for _ in range(25):
        stones = blink_stones(stones)
    print(len(stones))


if __name__ == "__main__":
    eleven_a()
