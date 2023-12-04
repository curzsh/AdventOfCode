import re
from word2number import w2n


with open('2023/day1/day1_input', 'r') as file:
  lines = [line.rstrip() for line in file]

numbers = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9")
num_re = r'(?:' + '|'.join(map(re.escape, numbers)) + r')'

reverse = [i[::-1] for i in numbers]
rev_num_re = r'(?:' + '|'.join(map(re.escape, reverse)) + r')'

def findNum(line):
  match = re.search(num_re, line.lower()).group()
  return str(w2n.word_to_num(match))

def findNumRev(line):
  match = re.search(rev_num_re, line.lower()).group()
  return str(w2n.word_to_num(match[::-1]))


total = 0
for line in lines:
    num = ''
    num += findNum(line)
    num += findNumRev(line[::-1])
    print(num)
    total += int(num)
    
print (total)
