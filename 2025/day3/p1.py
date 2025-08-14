import os
import re
import time

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('input', 'r') as file:
  lines = [line.rstrip() for line in file]

baseTime = time.time()

##############################################################################################
##################INSERT CODE HERE############################################################
##############################################################################################

pattern = r"mul\((\d+),(\d+)\)"
matches = []

for line in lines:
  matches += re.findall(pattern, line)

baseTotal = 0
for match in matches:   
  baseTotal += int(match[0]) * int(match[1])

###############################################################################################################
##############################################END MY CODE HEERE################################################
###############################################################################################################

baseEnd = time.time()

with open('input', 'r') as file:
    data = file.read()  # Read the entire file at once

aiTime = time.time()
#################################################################################################
##################INSERT AI CODE HERE############################################################
#################################################################################################

pattern = re.compile(r"mul\((\d+),(\d+)\)")
aiTotal = 0

for match in pattern.finditer(data):
    aiTotal += int(match.group(1)) * int(match.group(2))

###############################################################################################################
##############################################END AI CODE######################################################
###############################################################################################################
aiEnd = time.time()
print(f"#### Base Time: {baseEnd - baseTime:.20f} seconds")
print(f"#### AI Time:   {aiEnd - aiTime:.20f} seconds")

print("####  My Answer = " + str(baseTotal))
print("####  AI Answer = " + str(aiTotal))

#### Base Time: 0.00099897384643554688 seconds
#### AI Time:   0.00099945068359375000 seconds
####  My Answer = 162813399
####  AI Answer = 162813399