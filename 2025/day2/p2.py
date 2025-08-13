import os
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('input', 'r') as file:
  lines = [line.rstrip() for line in file]


def is_valid(seq):
    increasing = all(seq[j] < seq[j+1] for j in range(len(seq)-1))
    decreasing = all(seq[j] > seq[j+1] for j in range(len(seq)-1))
    adjacent = all(1 <= abs(seq[j] - seq[j+1]) <= 3 for j in range(len(seq)-1))
    return (increasing or decreasing) and adjacent

total = 0
for line in lines:
    numbers = [int(num) for num in line.split()]
    removed = False
    for idx in range(len(numbers)):
        temp_numbers = numbers[:idx] + numbers[idx+1:]
        if is_valid(temp_numbers):
            removed = True
            break
    if removed:
        total += 1

print(total)
