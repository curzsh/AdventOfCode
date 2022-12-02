with open('DAY2\day2_input') as file:
    lines = [line.rstrip() for line in file]
hPos=0
depth=0
for line in lines:
    temp = line.split(None,1)[0]
    num = int(line.split(None,1)[1])
    if temp == 'forward':
        hPos += num
    elif temp == 'up':
        depth += num
    else:
        depth -= num

print(abs(hPos*depth))
