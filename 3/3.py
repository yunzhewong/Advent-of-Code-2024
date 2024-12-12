import sys
import os
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.operate_on_lines import operate_on_lines

MAX_LENGTH = len("mul(123,123)")


def section_length_valid(section: str):
    length = len(section)
    return length <= 3 and len(section) >= 1


def get_value(string: str):
    if not string.startswith("mul("):
        return None

    numerical_section = string[len("mul(") : MAX_LENGTH]

    numbers = []
    start = 0
    for i, char in enumerate(numerical_section):
        if char == ",":
            section = numerical_section[start:i]
            if not section_length_valid(section) or len(numbers) != 0:
                return None
            numbers.append(int(section))
            start = i + 1
        elif char == ")":
            section = numerical_section[start:i]
            if not section_length_valid(section) or len(numbers) != 1:
                return None
            numbers.append(int(section))
            break
        else:
            current_char_str = str(char)
            if not current_char_str.isdigit():
                return None

    if len(numbers) != 2:
        print(numbers)
        return None
    return numbers[0] * numbers[1]


def three_a():
    total_sum = [0]

    def fn(stripped_line: str):
        for i in range(len(stripped_line)):
            if stripped_line[i] == "m":
                value = get_value(stripped_line[i : i + MAX_LENGTH])
                if value is not None:
                    total_sum[0] += value

    operate_on_lines(fn)

    print(total_sum[0])


if __name__ == "__main__":
    three_a()
