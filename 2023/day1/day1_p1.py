import re

with open('2023/day1/day1_input', 'r') as file:
  lines = [line.rstrip() for line in file]

total = 0

for line in lines:
  num = ''
  num += re.search(r'\d', line).group()
  num += re.search(r'\d', line[::-1]).group()
  total += int(num)

print(total)

