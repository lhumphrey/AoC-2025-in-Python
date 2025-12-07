import re
from functools import reduce

def process_number_col(num_col):
    num_list = []
    for col in range(len(num_col[0])):
        num_str = ''
        for row in range(len(num_col)):
            if num_col[row][col] != ' ':
                num_str += num_col[row][col]
        num_list.append(int(num_str))
    return num_list


# Main logic
with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]

operators = re.split(' +', lines[-1])
numbers_1 = []
for l in lines[:-1]:
    numbers_1.append([int (e) for e in re.split(' +', l.strip())])

operator_positions = []
for col in range(len(lines[-1])):
    if lines[-1][col] == '*' or lines[-1][col] == '+':
        operator_positions.append(col)
numbers_2 = []
for l in lines[:-1]:
    num_row = []
    for i in range(len(operator_positions) - 1):
        num_row.append([c for c in l[operator_positions[i] : operator_positions[i + 1] - 1]])
    num_row.append([c for c in l[operator_positions[-1]:]])
    numbers_2.append(num_row)


count1 = 0
for col in range(len(operators)):
    num_list = [numbers_1[row][col] for row in range(len(numbers_1))]
    if operators[col] == '+':
        count1 += reduce(lambda x, y: x + y, num_list)
    if operators[col] == '*':
        count1 += reduce(lambda x, y: x * y, num_list)
print('The total for part 1 is: ' + str(count1))

count2 = 0
for col in range(len(operators)):
    num_list = process_number_col([n[col] for n in numbers_2])
    if operators[col] == '+':
        count2 += reduce(lambda x, y: x + y, num_list)
    if operators[col] == '*':
        count2 += reduce(lambda x, y: x * y, num_list)
print('The total for part 2 is: ' + str(count2))