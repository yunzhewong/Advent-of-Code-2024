from typing import Callable


def operate_on_lines(callback: Callable[[str], None]) -> str:
  with open("input.txt") as f:
    lines = f.readlines()
    for line in lines: 
      stripped_line = line.strip()
      callback(stripped_line)