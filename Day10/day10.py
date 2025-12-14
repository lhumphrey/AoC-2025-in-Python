import re

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

# Main logic
with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]

light_panels = []
button_sets_1 = []
button_sets_2 = []
joltages = []
count1 = 0
for l in lines:
    m = re.search('[#.]+', l)
    light_str = l[m.start():m.end()]
    light_panels.append(light_str_to_num(light_str))
    f = re.finditer('[\\d,]+',l)
    num_strs = []
    for m in f:
        num_strs.append(m.group())
    button_list = []
    button_pos_list = []
    for n in num_strs[:-1]:
        button_pos = [int(b) for b in n.replace(',','')]
        button_pos_list.append(button_pos)
        button_list.append(button_pos_list_to_num(button_pos, len(light_str)))
    button_sets_1.append(button_list)
    button_sets_2.append(button_pos_list)
    joltages.append([int(b) for b in num_strs[-1].split(',')])
    num_pushes = find_solution_1(light_panels[-1], button_sets[-1])
    count1 += num_pushes

print('The count for Part 1 is: ' + str(count1))