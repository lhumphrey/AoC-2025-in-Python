from math import sqrt
from sortedcontainers import SortedKeyList

def distance(x1, x2):
    return sqrt((x1[0] - x2[0])**2 + (x1[1] - x2[1])**2 + (x1[2] - x2[2])**2)


def box_is_in_circuit(box, circuits):
    for i in range(len(circuits)):
        if box in circuits[i]:
            return i
    return -1


# Main logic
with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]

box_locs = []
for line in lines:
    box_locs.append([int(e) for e in line.split(',')])

box_pairs = SortedKeyList(key=lambda x: distance(x[0], x[1]))
for i in range(len(box_locs)):
    for j in range(i + 1,len(box_locs)):
        box_pairs.add([box_locs[i], box_locs[j]])

circuits = SortedKeyList(key=lambda x: -len(x))
circuits.add([box_pairs[0][0], box_pairs[0][1]])
for i in range(1,1000):
    box_pair = box_pairs[i]
    ind0 = box_is_in_circuit(box_pair[0], circuits)
    ind1 = box_is_in_circuit(box_pair[1], circuits)
    if ind0 < 0 and ind1 < 0:
        circuits.add([box_pair[0], box_pair[1]])
    elif ind0 >= 0 and ind1 < 0:
        tmp = circuits[ind0]
        circuits.pop(ind0)
        tmp.append(box_pair[1])
        circuits.add(tmp)
    elif ind0 < 0 and ind1 >= 0:
        tmp = circuits[ind1]
        circuits.pop(ind1)
        tmp.append(box_pair[0])
        circuits.add(tmp)
    elif ind0 != ind1:
        tmp0 = circuits[ind0]
        tmp1 = circuits[ind1]
        for second_circuit_box in tmp1:
            tmp0.append(second_circuit_box)
        if ind0 > ind1:
            circuits.pop(ind0)
            circuits.pop(ind1)
        else:
            circuits.pop(ind1)
            circuits.pop(ind0)
        circuits.add(tmp0)

count1 = 1
for i in range(3):
    count1 *= len(circuits[i])
print('The total for part 1 is: ' + str(count1))

for i in range(1000, len(box_pairs) - 1):
    box_pair = box_pairs[i]
    ind0 = box_is_in_circuit(box_pair[0], circuits)
    ind1 = box_is_in_circuit(box_pair[1], circuits)
    if ind0 < 0 and ind1 < 0:
        circuits.add([box_pair[0], box_pair[1]])
    elif ind0 >= 0 and ind1 < 0:
        tmp = circuits[ind0]
        circuits.pop(ind0)
        tmp.append(box_pair[1])
        circuits.add(tmp)
    elif ind0 < 0 and ind1 >= 0:
        tmp = circuits[ind1]
        circuits.pop(ind1)
        tmp.append(box_pair[0])
        circuits.add(tmp)
    elif ind0 != ind1:
        tmp0 = circuits[ind0]
        tmp1 = circuits[ind1]
        for second_circuit_box in tmp1:
            tmp0.append(second_circuit_box)
        if ind0 > ind1:
            circuits.pop(ind0)
            circuits.pop(ind1)
        else:
            circuits.pop(ind1)
            circuits.pop(ind0)
        circuits.add(tmp0)
    if len(circuits) == 1 and len(circuits[0]) == len(box_locs):
        break

print('The total for part 2 is: ' + str(box_pair[0][0] * box_pair[1][0]))