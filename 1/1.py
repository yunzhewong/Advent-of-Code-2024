import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.operate_on_lines import operate_on_lines

SPACE = "   "

def get_numbers(stripped_line: str):
      numbers = [int(i) for i in stripped_line.split(SPACE)]
      return numbers[0], numbers[1]

def one_a():
    list1 = []
    list2 = []

    def fn(stripped_line: str):
      first, second = get_numbers(stripped_line)
      list1.append(first)
      list2.append(second)

    operate_on_lines(fn)
   
    list1.sort()
    list2.sort()

    difference = [abs(list1[i] - list2[i]) for i in range(len(list1))]
    print(sum(difference))

def one_b():
  numbers = []
  counts = {}

  def fn(stripped_line: str):
    first, second = get_numbers(stripped_line)
    numbers.append(first)
    counts[second] = 1 + counts.get(second, 0)

  operate_on_lines(fn)

  sum = 0
  for number in numbers:
     sum += number * counts.get(number, 0)
  
  print(sum)



if __name__ == "__main__":
  one_b()