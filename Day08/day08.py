from math import sqrt
from sortedcontainers import SortedKeyList

def distance(x1, x2):
    return sqrt((x1[0] - x2[0])**2 + (x1[1] - x2[1])**2 + (x1[2] - x2[2])**2)


def box_is_in_circuit(box, circuits):
    for i in range(len(circuits)):
        for circuit_box_pair in circuits[i]:
            if box == circuit_box_pair[0] or box == circuit_box_pair[1]:
                return i
    return -1


# Main logic
with open('input_ex.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]

box_locs = []
for line in lines:
    box_locs.append([int(e) for e in line.split(',')])

box_pairs = SortedKeyList(key=lambda x: distance(x[0], x[1]))
for i in range(len(box_locs)):
    for j in range(i + 1,len(box_locs)):
        box_pairs.add([box_locs[i], box_locs[j]])

circuits = SortedKeyList(key=lambda x: len(x))
circuits.add([box_pairs[0]])
for i in range(1,10):
    box_pair = box_pairs[i]
    ind1 = box_is_in_circuit(box_pair[0], circuits)
    ind2 = box_is_in_circuit(box_pair[1], circuits)
    if ind1 < 0 and ind2 < 0:
        circuits.add([box_pair])
    elif ind1 >= 0 and ind2 < 0:
        circuits[ind1].append(box_pair)
    elif ind1 < 0 and ind2 >= 0:
        circuits[ind2].append(box_pair)
    elif ind1 != ind2:
        circuit_1 = circuits[ind1]
        circuit_2 = circuits[ind2]
        for circuit_2_box_pair in circuit_2:
            circuit_1.append(circuit_2_box_pair)
        circuits.pop(ind2)
        circuit_1.append(box_pair)

#for c in circuits:
#    print(c)
# 135 is too low

count1 = 1
for i in range(3):
    count1 *= len(circuits[i]) + 1
print('The total for part 1 is: ' + str(count1))

count2 = 0
print('The total for part 2 is: ' + str(count2))
