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
    iters = 25
    for i in range(iters):
        stones = blink_stones(stones)
    print(len(stones))


def compute_length_after_iters(stone, iters, memory: Dict[int, Dict[int, int]]):
    if iters == 0:
        return 1

    next_map = memory.get(stone, None)
    if next_map is not None:
        next_length = next_map.get(iters, None)
        if next_length is not None:
            return next_length

    next_stones = blink_stone(stone)
    length = 0
    for next_stone in next_stones:
        length += compute_length_after_iters(next_stone, iters - 1, memory)

    next_map = memory.get(stone, {})
    next_map[iters] = length
    memory[stone] = next_map
    return length


def eleven_b():
    stones = get_initial_stones()
    memory = {}
    iters = 75
    length = 0
    for stone in stones:
        length += compute_length_after_iters(stone, iters, memory)
    print(length)


if __name__ == "__main__":
    eleven_b()
