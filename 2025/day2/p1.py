import os
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('input', 'r') as file:
  lines = [line.rstrip() for line in file]

total = 0
for line in lines:
    numbers = [int(num) for num in line.split()]
    increasing = decreasing = adjacent = True
    prev = numbers[0]
    for curr in numbers[1:]:
        diff = curr - prev
        if diff > 0:
            decreasing = False
        elif diff < 0:
            increasing = False
        if not (1 <= abs(diff) <= 3):
            adjacent = False
        if (not increasing and not decreasing) or not adjacent:
            break
        prev = curr
    if (increasing or decreasing) and adjacent:
        total += 1

print(total)
