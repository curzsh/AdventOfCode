import re

with open('2025/day1/day1_input', 'r') as file:
  lines = [line.rstrip() for line in file]

total = 0
left_numbers = []
right_numbers = []

for line in lines:
    left, right = line.split()
    left_numbers.append(int(left))
    right_numbers.append(int(right))

  
number_map = {num: 0 for num in set(right_numbers)}

for right in right_numbers:
    if right in number_map:
        number_map[right] += 1
    else:
        number_map[right] = 1

for left in left_numbers:
    if left in number_map:
     total += left * number_map[left]

print(total)
