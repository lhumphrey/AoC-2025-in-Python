import re
import numpy as np
import pulp

def light_str_to_num(light_str):
    binary_str = ''
    for c in light_str:
        if c == '.':
            binary_str = binary_str + '0'
        elif c == '#':
            binary_str = binary_str + '1'
        else:
            raise RuntimeError('Invalid light string: ' + light_str)
    return int(binary_str, 2)


def button_pos_list_to_num(buttons, len):
    button_list = ['0'] * len
    for b in buttons:
        button_list[b] = '1'
    binary_str = ''
    for c in button_list:
        binary_str += '0' if c == '0' else '1'
    return int(binary_str, 2)


def bin_str(i):
    return format(i, 'b')


def find_solution_1(light_panel, buttons):
    step = []
    for button in buttons:
        step.append(light_panel ^ button)
        if light_panel ^ button == 0:
            return 1

    # This could be made more efficient. There's no reason to press
    # the same button twice, but I'm being lazy.
    counter = 2
    while counter < 100:
        step_tmp = []
        for s in step:
            for button in buttons:
                step_tmp.append(s ^ button)
                if step_tmp[-1] == 0:
                    return counter
        step = step_tmp
        counter += 1


def find_solution_2(button_vectors, joltages):

    A = np.array([np.array(bv) for bv in button_vectors])
    A = A.T
    B = np.array(joltages)
    prob = pulp.LpProblem("Integer_System", pulp.LpMinimize)
    x = [pulp.LpVariable(f'x{i}', lowBound=0, cat=pulp.LpInteger) for i in range(A.shape[1])]
    prob += pulp.lpSum(x)

    # Add the equality constraints
    for row_idx in range(A.shape[0]):
        prob += (pulp.lpSum(A[row_idx, col_idx] * x[col_idx] for col_idx in range(A.shape[1])) == B[row_idx])

    # Solve
    status = prob.solve()
    if pulp.LpStatus[status] == "Optimal":
        x_values = [var.varValue for var in x]
    else:
        raise RuntimeError

    return int(sum(x_values))


# Main logic
with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]

light_panels = []
button_sets_1 = []
button_sets_2 = []
joltages = []
count1 = 0
count2 = 0
for l in lines:
    m = re.search('[#.]+', l)
    light_str = l[m.start():m.end()]
    light_panels.append(light_str_to_num(light_str))
    f = re.finditer('[\\d,]+',l)
    num_strs = []
    for m in f:
        num_strs.append(m.group())
    button_list = []
    button_vec_list = []
    for n in num_strs[:-1]:
        button_pos = [int(b) for b in n.replace(',','')]
        button_list.append(button_pos_list_to_num(button_pos, len(light_str)))
        button_vec_tmp = [0] * len(light_str)
        for bp in button_pos:
            button_vec_tmp[bp] = 1
        button_vec_list.append(button_vec_tmp)
    button_sets_1.append(button_list)
    joltages.append([int(b) for b in num_strs[-1].split(',')])
    button_sets_2.append(button_vec_list)

    num_pushes = find_solution_1(light_panels[-1], button_sets_1[-1])
    count1 += num_pushes
    num_pushes = find_solution_2(button_sets_2[-1], joltages[-1])
    count2 += num_pushes
    # print(str(num_pushes))

print('The count for Part 1 is: ' + str(count1))
print('The count for Part 2 is: ' + str(count2))