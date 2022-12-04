with open('2022\day4\day4_input', 'r') as file:
  lines = [line.rstrip() for line in file]

import intspan

with open('2022\day4\day4_input', 'r') as file:
  lines = [line.rstrip() for line in file]

count = 0
for line in lines:
  work_shifts = line.split(',')
  set1 = set(intspan.intspan(work_shifts[0]))
  set2 = set(intspan.intspan(work_shifts[1]))

  if set1.intersection(set2):
    count += 1
  
print (count)