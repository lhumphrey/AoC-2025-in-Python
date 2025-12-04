def max_joltage_1(line):
    l = [int(i) for i in line]
    ind1 = l.index(max(l[0:-1]))
    ind2 = l.index(max(l[ind1 + 1:]))
    return 10 * l[ind1] + l[ind2]

def max_joltage_2(line, digits_to_go):
    l = [int(i) for i in line]
    max_ind = len(l) - digits_to_go
    ind1 = l.index(max(l[0:max_ind + 1]))
    val1 = l[ind1] * (10 ** (digits_to_go - 1))
    val2 = 0
    if digits_to_go > 1:
        val2 = max_joltage_2(line[ind1+1:], digits_to_go - 1)
    return val1 + val2

# Main logic
with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]

count1 = 0
for line in lines:
    count1 += max_joltage_1(line)
print('The total for part 1 is: ' + str(count1))

count2 = 0
for line in lines:
    val =  max_joltage_2(line, 12)
    count2 += val
print('The total for part 2 is: ' + str(count2))