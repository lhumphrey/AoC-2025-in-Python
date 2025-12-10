from math import sqrt
from sortedcontainers import SortedKeyList

def area(x1, x2):
    return (abs(x1[0] - x2[0]) + 1) * (abs(x1[1] - x2[1]) + 1)


# Main logic
with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]

corner_locs = []
for line in lines:
    corner_locs.append([int(e) for e in line.split(',')])
print(corner_locs)

corner_pairs = SortedKeyList(key=lambda x: -area(x[0], x[1]))
for i in range(len(corner_locs)):
    for j in range(i + 1,len(corner_locs)):
        corner_pairs.add([corner_locs[i], corner_locs[j]])

count1 = area(corner_pairs[0][0], corner_pairs[0][1])
print('The total for part 1 is: ' + str(count1))
# 4748985168
