with open('2022\day3\day3_input', 'r') as file:
  lines = [line.rstrip() for line in file]

priority = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

answer = 0
for line in lines:
  firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
  common = ''.join(set(firstpart).intersection(secondpart))
  answer += priority.index(common)

print (answer)
  
