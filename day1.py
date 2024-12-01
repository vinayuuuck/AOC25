def countdistance(filename):
  with open(filename) as f:
    lines = f.readlines()
    colr = []
    coll = []
    distance = 0
    for line in lines:
      ap1, ap2 = line.split()
      colr.append(ap1)
      coll.append(ap2)
    colr.sort()
    coll.sort()
    for i in range(0, len(colr)):
      distance += abs(int(colr[i]) - int(coll[i]))

  return distance

print(countdistance('./inputs/d1input.txt'))