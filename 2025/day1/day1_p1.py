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

left_numbers.sort();
right_numbers.sort();

for left, right in zip(left_numbers, right_numbers):
    total += abs(left-right)

print(total)
