import os
import re
import time

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('input', 'r') as file:
  lines = [line.rstrip() for line in file]

start = time.time()


pattern = r".*?mul\((\d+),(\d+)\)"
matches = []

for line in lines:
  matches += re.finditer(pattern, line)
  
total = 0
enabled = True
for match in matches:   
    if "don't()" in match.group(0):
        enabled = False
    elif "do()" in match.group(0):
        enabled = True

    if enabled:
        total += int(match[1]) * int(match[2])

print(total)

end = time.time()
print(f"Elapsed time: {end - start:.20f} seconds")

#base time:         Elapsed time: 0.00149917602539062500 seconds
#AI optimized time: Elapsed time: 0.00150012969970703125 seconds

import os
import re
import time

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('input', 'r') as file:
    data = file.read()  # Read entire file at once

start = time.time()

pattern = re.compile(r"(.*?)(mul\((\d+),(\d+)\))")
total = 0
enabled = True

for match in pattern.finditer(data):
    context = match.group(1)
    mul_str = match.group(2)
    x = int(match.group(3))
    y = int(match.group(4))

    if "don't()" in context:
        enabled = False
    elif "do()" in context:
        enabled = True

    if enabled:
        total += x * y

print(total)

end = time.time()
print(f"Elapsed time: {end - start:.20f} seconds")