import os
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('input', 'r') as file:
  lines = [line.rstrip() for line in file]

def is_valid(seq):
    if len(seq) < 2:
        return False
    increasing = True
    decreasing = True
    adjacent = True
    for j in range(1, len(seq)):
        if seq[j] > seq[j-1]:
            decreasing = False
        elif seq[j] < seq[j-1]:
            increasing = False
        if not (1 <= abs(seq[j] - seq[j-1]) <= 3):
            adjacent = False
        if not (increasing or decreasing) or not adjacent:
            return False
    return (increasing or decreasing) and adjacent

total = 0
for line in lines:
    numbers = [int(num) for num in line.split()]
    valid_with_removal = False
    for idx in range(len(numbers)):
        temp_numbers = numbers[:idx] + numbers[idx+1:]
        if is_valid(temp_numbers):
            valid_with_removal = True
            break
    if valid_with_removal:
        total += 1

print(total)
