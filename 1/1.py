from typing import Callable


SPACE = "   "

def operate_on_lines(callback: Callable[[str], None]) -> str:
  with open("input.txt") as f:
    lines = f.readlines()
    for line in lines: 
      stripped_line = line.strip()
      callback(stripped_line)

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