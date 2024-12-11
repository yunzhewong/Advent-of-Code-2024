SPACE = "   "

def one_a():
  with open("input.txt") as f:
    lines = f.readlines()

    list1 = []
    list2 = []
    for line in lines: 
      stripped_line = line.strip()
      numbers = [int(i) for i in stripped_line.split(SPACE)]
      list1.append(numbers[0])
      list2.append(numbers[1])

    list1.sort()
    list2.sort()

    difference = [abs(list1[i] - list2[i]) for i in range(len(list1))]
    print(sum(difference))



if __name__ == "__main__":
  one_a()