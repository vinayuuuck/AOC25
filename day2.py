data:list[list[int]] = []
with open('./inputs/d2input.txt') as f:
  for line in f:
    data.append(list(map(int, line.strip().split())))

# Part 1
def safe1(level:list[int]) -> int:
  return all(1<=abs(a-b)<=3 for a,b in zip(level, level[1:])) and (level == sorted(level) or level == sorted(level, reverse=True))

def safe2(level:list[int]) -> int:
  return any(safe1(level[:i] + level[i+1:]) for i in range(len(level)))

print(sum(safe1(level) for level in data))
print(sum(safe2(level) for level in data))