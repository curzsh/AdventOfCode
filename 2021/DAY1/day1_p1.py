count = 0
with open('DAY1\day1_input') as file:
    lines = [line.rstrip() for line in file]

for curNum, nextNum in zip(lines, lines[1:]):
    if int(nextNum) > int(curNum):
        count +=1 

print(count)
