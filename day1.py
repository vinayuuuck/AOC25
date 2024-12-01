def countdistance(filename : str) -> int:
  colr : list[int] = []
  coll : list[int] = []
  distance : int = 0
  with open(filename) as f:
    lines : list = f.readlines()

  for line in lines:
    ap1, ap2 = line.split()
    colr.append(int(ap1))
    coll.append(int(ap2))

  colr.sort()
  coll.sort()
  
  for i in range(0, len(colr)):
    distance += abs(colr[i] - coll[i])

  return distance

def similarityscore(filename : str) -> int:
  dictr : dict[int, int] = {}
  coll : list[int] = []
  score : int = 0
  with open(filename) as f:
    lines : list = f.readlines()

  for line in lines:
    ap1, ap2 = line.split()
    coll.append(int(ap2))
    if int(ap1) not in dictr:
      dictr[int(ap1)] = 1
    else:
      dictr[int(ap1)] += 1
  
  for idx, elem in enumerate(coll):
    score += dictr.get(int(elem), 0)*elem
  
  return score

print(countdistance('./inputs/d1input.txt'))
print(similarityscore('./inputs/d1input.txt'))
