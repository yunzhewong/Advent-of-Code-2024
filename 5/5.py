import sys
import os
from typing import Callable, Dict, List, Tuple

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.operate_on_lines import operate_on_lines, operate_on_test


class FiveAState:
    def __init__(self):
        self.found_space = 0
        self.rules: Dict[int, List[int]] = {}
        self.total = 0


def parse_rule(line: str):
    numbers = [int(i) for i in line.split("|")]
    return numbers[0], numbers[1]


def parse_updates(line: str):
    return [int(i) for i in line.split(",")]


def five_a():
    state = FiveAState()

    def fn(line: str):
        if line == "":
            state.found_space = True
            return

        if not state.found_space:
            x, y = parse_rule(line)

            arr = state.rules.get(x, [])
            arr.append(y)
            state.rules[x] = arr
            return

        updates = parse_updates(line)

        for i in range(len(updates)):
            current_update = updates[i]
            later_updates = updates[i + 1 :]

            matching_rules = state.rules.get(current_update, [])

            for update in later_updates:
                if update not in matching_rules:
                    return

        middle_index = int((len(updates) - 1) / 2)
        middle_page = updates[middle_index]

        state.total += middle_page

    operate_on_lines(fn)

    print(state.total)


if __name__ == "__main__":
    five_a()
