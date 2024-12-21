import math
import os
import sys
import time
from enum import Enum
from typing import Callable, Dict, List, Tuple

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.operate_on_lines import operate_on_lines, operate_on_test

EPSILON = 0.01


def close_to_int(l: float):
    return abs(l - round(l)) < EPSILON


def parse_button_line(l: str):
    first_plus_index = l.find("+")
    first_comma_index = l.find(",")
    x = int(l[first_plus_index + 1 : first_comma_index])

    second_plus_index = l.find("+", first_comma_index + 1)
    y = int(l[second_plus_index + 1 :])
    return (x, y)


def parse_prize_line(l: str):
    first_equal_index = l.find("=")
    first_comma_index = l.find(",")
    x = int(l[first_equal_index + 1 : first_comma_index])

    second_equal_index = l.find("=", first_equal_index + 1)
    y = int(l[second_equal_index + 1 :])
    return (x, y)


def parse_input():
    games = []

    abpi = [None, None, None, 0]

    def fn(l: str):
        if abpi[3] % 4 == 0:
            abpi[0] = parse_button_line(l)
        if abpi[3] % 4 == 1:
            abpi[1] = parse_button_line(l)
        if abpi[3] % 4 == 2:
            abpi[2] = parse_prize_line(l)
        if abpi[3] % 4 == 3:
            games.append((abpi[0], abpi[1], abpi[2]))
        abpi[3] += 1

    operate_on_lines(fn)
    games.append((abpi[0], abpi[1], abpi[2]))

    return games


def dot(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]


def get_game_solution(game):
    # [x_A; y_A] * A + [x_B; y_B] * B = [x_P; y_P]
    # [x_A x_B; y_A y_B] * [A; B] = [x_P; y_P]
    x_A, y_A = game[0]
    x_B, y_B = game[1]
    x_P, y_P = game[2]

    idet = 1 / (x_A * y_B - y_A * x_B)

    A = idet * (y_B * x_P - x_B * y_P)
    B = idet * (-y_A * x_P + x_A * y_P)
    if close_to_int(A) and close_to_int(B):

        return round(A), round(B)

    return None


def evaluate_solution_cost(solution):
    return solution[0] * 3 + solution[1]


def thirteen_a():
    games = parse_input()
    total = 0

    for game in games:
        solution = get_game_solution(game)
        # print(solution)
        if solution is None:
            continue
        cost = evaluate_solution_cost(solution)
        total += cost

    print(total)


if __name__ == "__main__":
    thirteen_a()
