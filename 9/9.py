import os
import sys
import time
from enum import Enum
from typing import Callable, Dict, List, Tuple

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.operate_on_lines import operate_on_lines, operate_on_test


def read_line():
    lines = [""]

    def fn(l):
        lines[0] = l

    operate_on_lines(fn)
    return lines[0]


def get_disk_map(line):
    disk_map = []
    is_file = True
    id = 0

    for char in line:
        if is_file:
            disk_map.append((int(char), id))
            id += 1
        else:
            disk_map.append((int(char), -1))
        is_file = not is_file

    return disk_map


def collapse_map_a(disk_map: List[Tuple[int, int]]):
    forward_index = 1
    reverse_index = -1
    output = [disk_map[0]]

    while True:
        replace_count, replace_item = disk_map[forward_index]

        if replace_item != -1:
            if replace_count == 0:
                break
            output.append(disk_map[forward_index])
            forward_index += 1
            continue

        new_items = []

        while replace_count != 0:
            if len(disk_map) + reverse_index <= forward_index:
                break

            count, item = disk_map[reverse_index]
            if count == 0 or item == -1:
                reverse_index -= 1
                continue

            if count >= replace_count:
                new_items.append((replace_count, item))
                disk_map[reverse_index] = (count - replace_count, item)
                replace_count = 0
            else:
                new_items.append((count, item))
                replace_count -= count
                disk_map[reverse_index] = (0, item)

        output += new_items
        forward_index += 1

    return output


def compute_checksum(collapsed):
    total = 0
    position = 0

    for pair in collapsed:
        count, item = pair

        if item != -1:
            for i in range(count):
                total += item * (position + i)
        position += count

    return total


def nine_a():
    line = read_line()
    disk_map = get_disk_map(line)
    collapsed = collapse_map_a(disk_map)
    total = compute_checksum(collapsed)
    print(total)


def find_slot(disk_map, count, reverse_index):
    for i in range(reverse_index):
        slot_count, slot_item = disk_map[i]

        if slot_item != -1:
            continue

        if slot_count >= count:
            return i

    return -1


def combine_empties(disk_map: List[Tuple[int, int]]):
    unemptied = []

    running_count = 0
    for pair in disk_map:
        count, item = pair

        if item != -1:
            if running_count != 0:
                unemptied.append((running_count, -1))
                running_count = 0
            unemptied.append(pair)
        else:
            running_count += count

    if running_count != 0:
        unemptied.append((running_count, -1))
    return unemptied


def find_index(id, disk_map):
    for i in range(len(disk_map)):
        if disk_map[i][1] == id:
            return i
    return -1


def collapse_map_b(disk_map: List[Tuple[int, int]]):
    ids = [id for (_, id) in disk_map]
    current_id = max(ids)

    while current_id != 0:
        print(current_id)
        disk_map = combine_empties(disk_map)

        id_index = find_index(current_id, disk_map)

        move_count, move_item = disk_map[id_index]

        if move_item == -1:
            current_id -= 1
            continue

        slot_index = find_slot(disk_map, move_count, id_index)

        if slot_index == -1:
            current_id -= 1
            continue

        slot_count, _ = disk_map[slot_index]

        disk_map[slot_index] = (slot_count - move_count, -1)
        disk_map[id_index] = (move_count, -1)
        disk_map.insert(slot_index, (move_count, move_item))
        current_id -= 1

    return disk_map


def nine_b():
    line = read_line()
    disk_map = get_disk_map(line)
    collapsed = collapse_map_b(disk_map)
    total = compute_checksum(collapsed)
    print(total)


if __name__ == "__main__":
    nine_b()
