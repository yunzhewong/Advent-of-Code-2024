import sys
import os
from typing import Callable, Dict, List, Tuple

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.operate_on_lines import operate_on_lines, operate_on_test


class State:
    def __init__(self):
        self.found_space = 0
        self.rules: Dict[int, List[int]] = {}
        self.total = 0


def parse_rule(line: str):
    numbers = [int(i) for i in line.split("|")]
    return numbers[0], numbers[1]


def parse_updates(line: str):
    return [int(i) for i in line.split(",")]


def get_invalidating_update(rules: Dict[int, List[int]], updates: List[int]):
    for i in range(len(updates)):
        current_update = updates[i]
        later_updates = updates[i + 1 :]

        matching_rules = rules.get(current_update, [])

        for later_update in later_updates:
            if later_update not in matching_rules:
                return current_update, later_update

    return None


def updates_valid(rules: Dict[int, List[int]], updates: List[int]):
    return get_invalidating_update(rules, updates) is None


def get_middle_value(updates: List[int]):
    middle_index = int((len(updates) - 1) / 2)
    return updates[middle_index]


def parse_file():
    state = State()

    all_updates = []

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
        all_updates.append(updates)

    operate_on_lines(fn)

    return state.rules, all_updates


def five_a():
    rules, all_updates = parse_file()

    total = 0
    for updates in all_updates:
        if not updates_valid(rules, updates):
            continue

        total += get_middle_value(updates)

    print(total)


def fix_incorrect_updates(rules: Dict[int, List[int]], updates: List[int]):
    while True:
        invalidating_update = get_invalidating_update(rules, updates)

        if invalidating_update is None:
            break

        current_update, later_update = invalidating_update

        invalid_update_index = updates.index(later_update)
        updates.pop(invalid_update_index)
        update_index = updates.index(current_update)
        updates.insert(update_index, later_update)

    return updates


def five_b():
    rules, all_updates = parse_file()

    total = 0

    for updates in all_updates:
        if updates_valid(rules, updates):
            continue

        fix_incorrect_updates(rules, updates)

        total += get_middle_value(updates)

    print(total)


if __name__ == "__main__":
    five_b()
