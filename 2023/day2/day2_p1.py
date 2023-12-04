import re
from word2number import w2n

with open('2023/day2/day2_input', 'r') as file:
  lines = [line.rstrip() for line in file]


RED_CUBE_TOTAL = 12
GREEN_CUBE_TOTAL = 13
BLUE_CUBE_TOTAL = 14

def setIsGood(line):
  list = re.findall(r'(\d{1,}) (red|green|blue)', line)
  for entry in list:
    if entry[1] == 'red' and int(entry[0]) > RED_CUBE_TOTAL:
      print(line)
      return False
    if entry[1] == 'green' and int(entry[0]) > GREEN_CUBE_TOTAL:
      print(line)
      return False
    if entry[1] == 'blue' and int(entry[0]) > BLUE_CUBE_TOTAL: 
      print(line)
      return False
    
  return True

def evalGame(line):
  game =  re.search(r'Game (\d+):', line).group(1)
  print(game)

  if(setIsGood(re.sub(r'Game (\d+):', '', line))):
    return w2n.word_to_num(game)
  else:
    return 0

total = 0
for line in lines:
  total += evalGame(line)

print(total)
