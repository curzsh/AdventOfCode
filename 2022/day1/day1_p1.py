
with open('2022/day1/day1_input', 'r') as file:
  lines = [line.rstrip() for line in file]

index = 0
elf_calories = [0]
for line in lines:
  if not line:
    index += 1
    elf_calories.append(0)
  else:
    elf_calories[index] += int(line)

print (max(elf_calories))
