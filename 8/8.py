import os
import sys
import time
from enum import Enum
from typing import Callable, Dict, List, Tuple

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.operate_on_lines import operate_on_lines, operate_on_test


def parse_file():
    nodes: Dict[str, List[Tuple[int, int]]] = {}

    size = [0, 0]

    def fn(line):
        if size[1] == 0:
            size[1] = len(line)

        for i in range(len(line)):
            char = line[i]
            if char == ".":
                continue

            arr = nodes.get(char, [])
            arr.append((size[0], i))
            nodes[char] = arr
        size[0] += 1

    operate_on_lines(fn)

    return (size[0], size[1]), nodes


def in_board(size, position):
    return (
        position[0] >= 0
        and position[0] < size[0]
        and position[1] >= 0
        and position[1] < size[1]
    )


def evaluate_antinodes(antennas):
    antinodes = []

    for i in range(len(antennas)):
        for j in range(i + 1, len(antennas)):
            antinodes += get_antinodes(antennas[i], antennas[j])

    return antinodes


def get_antinodes(antenna1, antenna2):
    oneToTwo = (antenna2[0] - antenna1[0], antenna2[1] - antenna1[1])
    anti1 = (antenna1[0] - oneToTwo[0], antenna1[1] - oneToTwo[1])
    anti2 = (antenna2[0] + oneToTwo[0], antenna2[1] + oneToTwo[1])

    return [anti1, anti2]


def eight_a():
    size, nodes = parse_file()

    all_antinodes = []

    for frequency in nodes.keys():
        antinodes = evaluate_antinodes(nodes[frequency])
        for antinode in antinodes:
            if not in_board(size, antinode):
                continue

            if antinode in all_antinodes:
                continue

            all_antinodes.append(antinode)

    print(len(all_antinodes))


if __name__ == "__main__":
    eight_a()
