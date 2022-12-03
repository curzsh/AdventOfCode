with open('2022\day3\day3_input', 'r') as file:
  lines = [line.rstrip() for line in file]

priority = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

#turn list into groups of 3 lines each
groups = list(zip(*[iter(lines)]*3))

answer = 0 
for group in groups:
  #intersects each string to find common character among all 3 strings. 
  common = ''.join(set(group[0]).intersection(group[1], group[2]))
  answer += priority.index(common)

print (answer)
