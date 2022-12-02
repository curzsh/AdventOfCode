with open('DAY2\day2_input') as file:
    lines = [line.rstrip() for line in file]
hPos=0
depth=0
aim=0
for line in lines:
    temp = line.split(None,1)[0]
    num = int(line.split(None,1)[1])
    if temp == 'forward':
        hPos += (num)
        depth += (num*aim)
    elif temp == 'up':
        aim -= num
        print(aim)
    else:
        aim += num
        print(aim)

print(abs(hPos*depth))