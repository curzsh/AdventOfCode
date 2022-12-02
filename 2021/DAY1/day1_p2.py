count = 0
with open('DAY1\day1_input') as file:
    lines = [line.rstrip() for line in file]

temp = int(lines[0]) + int(lines[1]) + int(lines[2])

for one, two, three in zip(lines[1:], lines[2:], lines[3:]):
    if int(one) + int(two) + int(three) > temp:
        count += 1
    temp = int(one) + int(two) + int(three)

print(count)
