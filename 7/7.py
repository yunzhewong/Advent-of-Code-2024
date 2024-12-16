import os
import sys
import time
from enum import Enum
from typing import Callable, Dict, List, Tuple

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.operate_on_lines import operate_on_lines, operate_on_test


class Operator(Enum):
    Add = 0
    Multiply = 1
    Concatenate = 2


def split_line(line: str):
    sections = line.split(":")
    total = int(sections[0])
    numbers = [int(i) for i in sections[1].split(" ")[1:]]
    return total, numbers


def increment_signs(signs, option_count):
    signs[-1] += 1

    for i in range(len(signs)):
        if i == len(signs) - 1:
            continue

        if signs[-1 - i] == option_count:
            signs[-1 - i] = 0
            signs[-1 - i - 1] += 1

    return signs


def evaluate_option(numbers: List[int], signs: List[int]):
    total = numbers[0]

    for i in range(len(signs)):
        sign = signs[i]
        next = numbers[i + 1]
        if sign == Operator.Multiply.value:
            total *= next
        elif sign == Operator.Add.value:
            total += next
        elif sign == Operator.Concatenate.value:
            total = int(str(total) + str(next))

    return total


def numbers_meet_total(numbers: List[int], total: int, operator_options: int):
    signs = [0 for _ in range(len(numbers) - 1)]

    methods = operator_options ** len(signs)

    for _ in range(methods):
        if evaluate_option(numbers, signs) == total:
            return True
        signs = increment_signs(signs, operator_options)

    return False


def seven_a():
    sum = [0]

    def fn(line):
        total, numbers = split_line(line)
        if numbers_meet_total(numbers, total, 2):
            sum[0] += total

    operate_on_lines(fn)

    print(sum[0])


def seven_b():
    sum = [0, 0]

    def fn(line):
        total, numbers = split_line(line)
        if numbers_meet_total(numbers, total, 3):
            sum[0] += total
        sum[1] += 1
        print(sum[1])

    operate_on_lines(fn)

    print(sum[0])


if __name__ == "__main__":
    seven_b()
