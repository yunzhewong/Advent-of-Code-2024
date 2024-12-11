import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.operate_on_lines import operate_on_lines


def same_sign(number1, number2):
    return number1 * number2 >= 0


def two_a():
    total_safe = [0]

    def fn(stripped_line: str):
        numbers = [int(i) for i in stripped_line.split(" ")]

        first_diff = numbers[1] - numbers[0]

        for i in range(len(numbers) - 1):
            diff = numbers[i + 1] - numbers[i]

            if not same_sign(first_diff, diff):
                return

            if abs(diff) > 3 or abs(diff) < 1:
                return

        total_safe[0] += 1

    operate_on_lines(fn)

    print(total_safe[0])


if __name__ == "__main__":
    two_a()
