import math
import os
import sys
import time
from enum import Enum
from typing import Callable, Dict, List, Tuple

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.operate_on_lines import operate_on_lines, operate_on_test


class State:
    def __init__(self):
        self.A = 0
        self.B = 0
        self.C = 0
        self.operations = []
        self.pointer = 0
        self.output = []

    def __str__(self):
        return f"{self.A}, {self.B}, {self.C}, {self.operations}"

    def has_operations(self):
        return self.pointer + 1 < len(self.operations)

    def adv_output(self, combo_operand):
        numerator = self.A
        denominator = 2**combo_operand
        return int(numerator / denominator)

    def get_combo_operand(self, literal_operand):
        if literal_operand <= 3:
            return literal_operand
        if literal_operand == 4:
            return self.A
        if literal_operand == 5:
            return self.B
        if literal_operand == 6:
            return self.C
        raise Exception("Not possible")

    def apply_operation(self):
        opcode = self.operations[self.pointer]
        literal_operand = self.operations[self.pointer + 1]

        combo_operand = self.get_combo_operand(literal_operand)

        if opcode == 0:
            self.A = self.adv_output(combo_operand)
        if opcode == 1:
            self.B = self.B ^ literal_operand
        if opcode == 2:
            self.B = combo_operand % 8
        if opcode == 3:
            if self.A != 0:
                self.pointer = literal_operand - 2
        if opcode == 4:
            self.B = self.B ^ self.C
        if opcode == 5:
            self.output.append(combo_operand % 8)
        if opcode == 6:
            self.B = self.adv_output(combo_operand)
        if opcode == 7:
            self.C = self.adv_output(combo_operand)
        self.pointer += 2


def parse_register(l: str):
    return int(l.split(" ")[2])


def parse_input():

    state = State()
    count = [0]

    def fn(l):
        if count[0] == 0:
            state.A = parse_register(l)
        if count[0] == 1:
            state.B = parse_register(l)
        if count[0] == 2:
            state.C = parse_register(l)
        if count[0] == 4:
            state.operations = [int(i) for i in l.split(" ")[1].split(",")]
            state.pointer = 0
        count[0] += 1

    operate_on_lines(fn)

    return state


def seventeen_a():
    state = parse_input()

    while state.has_operations():
        state.apply_operation()

    print(",".join([str(i) for i in state.output]))


if __name__ == "__main__":
    seventeen_a()
