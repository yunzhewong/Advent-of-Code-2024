import sys
import os
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.operate_on_lines import operate_on_lines


def same_sign(number1, number2):
    return number1 * number2 >= 0


def valid_range(diff):
    return abs(diff) <= 3 and abs(diff) >= 1


def get_numbers(line: str):
    return [int(i) for i in line.split(" ")]


def is_safe(numbers):
    first_diff = numbers[1] - numbers[0]

    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]

        if not same_sign(first_diff, diff):
            return False

        if not valid_range(diff):
            return False

    return True


def two_a():
    total_safe = [0]

    def fn(stripped_line: str):
        numbers = get_numbers(stripped_line)

        if is_safe(numbers):
            total_safe[0] += 1

    operate_on_lines(fn)

    print(total_safe[0])


def identify_dominant_number_sign(numbers: List[int]):
    if len(numbers) < 4:
        return None
    start_diffs = [numbers[i + 1] - numbers[i] for i in range(3)]
    start_diffs.sort()
    return start_diffs[1]


def two_b():
    total_safe = [0]

    def fn(stripped_line: str):
        numbers = get_numbers(stripped_line)

        if is_safe(numbers):
            total_safe[0] += 1
            return

        for i in range(len(numbers)):
            new_numbers = numbers[:i] + numbers[i + 1 :]
            safe = is_safe(new_numbers)
            if safe:
                total_safe[0] += 1
                return

    operate_on_lines(fn)

    print(total_safe[0])


if __name__ == "__main__":
    two_b()
