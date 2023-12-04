import re
from word2number import w2n

with open('2023/day2/day2_input', 'r') as file:
  lines = [line.rstrip() for line in file]

def evalGame(line):
  list = re.findall(r'(\d{1,}) (red|green|blue)', line)
  maxRed = 0
  maxBlue = 0
  maxGreen = 0

  for entry in list:
    if entry[1] == 'red' and int(entry[0]) > maxRed:
      maxRed = int(entry[0])

    if entry[1] == 'green' and int(entry[0]) > maxGreen:
      maxGreen = int(entry[0])

    if entry[1] == 'blue' and int(entry[0]) > maxBlue: 
      maxBlue = int(entry[0])

  return maxRed * maxGreen * maxBlue

def minCubes(line):
  line = re.sub(r'Game (\d+):', '', line)
  return evalGame(line)

total = 0
for line in lines:
  total += minCubes(line)

print(total)
