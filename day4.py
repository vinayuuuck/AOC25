import itertools

data: list[list[str]] = []
with open('./inputs/d4input.txt') as f:
  lines = f.read().split('\n')
  for line in lines:
    data.append(list(line))

# Part 1
indices = [-3, -2, -1, 0, 1, 2, 3]

# check for XMAS
xmascount = 0
cross_mas_count = 0
for i, e in enumerate(data):
  for j, c in enumerate(e):
    if j+3 < len(e) and data[i][j] == "X" and data[i][j+1] == "M" and data[i][j+2] == "A" and data[i][j+3] == "S":
      xmascount += 1
    if i+3 < len(data) and data[i][j] == "X" and data[i+1][j] == "M" and data[i+2][j] == "A" and data[i+3][j] == "S":
      xmascount += 1
    if i+3 < len(data) and j+3 < len(e) and data[i][j] == "X" and data[i+1][j+1] == "M" and data[i+2][j+2] == "A" and data[i+3][j+3] == "S":
      xmascount += 1
    if i-3 >= 0 and j+3 < len(e) and data[i][j] == "X" and data[i-1][j+1] == "M" and data[i-2][j+2] == "A" and data[i-3][j+3] == "S":
      xmascount += 1
    if i-3 >= 0 and data[i][j] == "X" and data[i-1][j] == "M" and data[i-2][j] == "A" and data[i-3][j] == "S":
      xmascount += 1
    if j-3 >= 0 and data[i][j] == "X" and data[i][j-1] == "M" and data[i][j-2] == "A" and data[i][j-3] == "S":
      xmascount += 1
    if i+3 < len(data) and j-3 >= 0 and data[i][j] == "X" and data[i+1][j-1] == "M" and data[i+2][j-2] == "A" and data[i+3][j-3] == "S":
      xmascount += 1
    if i-3 >= 0 and j-3 >= 0 and data[i][j] == "X" and data[i-1][j-1] == "M" and data[i-2][j-2] == "A" and data[i-3][j-3] == "S":
      xmascount += 1

    # Part 2
    if i+2 < len(data) and j+2 < len(e) and data[i][j] == "M" and data[i][j+2] == "S" and data[i+2][j] == "M" and data[i+2][j+2] == "S" and data[i+1][j+1] == "A":
      cross_mas_count += 1
    
    if i+2 < len(data) and j+2 < len(e) and data[i][j] == "M" and data[i][j+2] == "M" and data[i+2][j] == "S" and data[i+2][j+2] == "S" and data[i+1][j+1] == "A":  
      cross_mas_count += 1

    if i+2 < len(data) and j+2 < len(e) and data[i][j] == "S" and data[i][j+2] == "M" and data[i+2][j] == "S" and data[i+2][j+2] == "M" and data[i+1][j+1] == "A":
      cross_mas_count += 1

    if i+2 < len(data) and j+2 < len(e) and data[i][j] == "S" and data[i][j+2] == "S" and data[i+2][j] == "M" and data[i+2][j+2] == "M" and data[i+1][j+1] == "A":
      cross_mas_count += 1
      
print(xmascount)
print(cross_mas_count)
