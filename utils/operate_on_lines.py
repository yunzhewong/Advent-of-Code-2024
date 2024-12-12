from typing import Callable


def operate_on_lines(callback: Callable[[str], None]):
    operate_on_file("input.txt", callback)


def operate_on_test(callback: Callable[[str], None]):
    operate_on_file("testinput.txt", callback)


def operate_on_file(filename: str, callback: Callable[[str], None]):
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            callback(stripped_line)
