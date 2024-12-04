import re

with open('./inputs/d3input.txt') as f:
  data = f.read()

matches = re.findall("mul\(\d{1,3}\,\d{1,3}\)", data)
mulsum = 0
for match in matches:
  a, b = map(int, match[4:-1].split(','))
  mulsum += a*b
print(mulsum)

matches2 = re.findall("mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don\'t\(\)", data)
mulsum = 0
doflag = True
for match2 in matches2:
  if match2 == "do()":
    doflag = True
  elif match2 == "don't()":
    doflag = False
  else:
    if doflag:
      a, b = map(int, match2[4:-1].split(','))
      mulsum += a*b
print(mulsum)