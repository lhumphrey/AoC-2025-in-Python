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


def button_str_to_num(buttons, len):
    button_list = ['0'] * len
    for b in buttons:
        button_list[b] = '1'
    binary_str = ''
    for c in button_list:
        binary_str += '0' if c == '0' else '1'
    return int(binary_str, 2)


# Main logic
with open('input_ex.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]

lights = []
buttons = []
joltages = []
for l in lines:
    m = re.search('[#.]+', l)
    light_str = l[m.start():m.end()]
    print(light_str)
    lights.append(light_str_to_num(light_str))
    f = re.finditer('[\\d,]+',l)
    num_strs = []
    for m in f:
        num_strs.append(m.group())
    button_list = []
    print(num_strs)
    for n in num_strs[:-1]:
        button_list.append(button_str_to_num([int(b) for b in n.replace(',','')], len(light_str)))
    buttons.append(button_list)
    joltages.append([int(b) for b in num_strs[-1].split(',')])

for l in lights:
    print(format(l, 'b'))
for b in buttons:
    for mb in b:
        print(format(mb, 'b'))
print(joltages)