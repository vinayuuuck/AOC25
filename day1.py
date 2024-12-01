def countdistance(filename : str) -> int:
  colr : list[int] = []
  coll : list[int] = []
  distance : int = 0
  with open(filename) as f:
    lines : list = f.readlines()

  for line in lines:
    ap1, ap2 = line.split()
    colr.append(ap1)
    coll.append(ap2)
  colr.sort()
  coll.sort()
  for i in range(0, len(colr)):
    distance += abs(int(colr[i]) - int(coll[i]))

  return distance

def similarityscore(filename : str) -> int:
  return 0

print(countdistance('./inputs/d1input.txt'))