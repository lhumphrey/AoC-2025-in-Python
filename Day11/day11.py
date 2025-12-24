import re
from functools import lru_cache

output_to_inputs = dict()
input_to_outputs = dict()

# Main logic
with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]

pattern = re.compile(r"([a-z]+)")
for l in lines:
    matches = pattern.findall(l)
    input_to_outputs[matches[0]] = matches[1:]

for key, value in input_to_outputs.items():
    for v in value:
        if v not in output_to_inputs:
            output_to_inputs[v] = [key]
        else:
            output_to_inputs[v] = output_to_inputs[v] + [key]

@lru_cache(maxsize=None)   # Memoization with unlimited cache
def get_paths_to_you(key):
    inputs = output_to_inputs[key]
    paths = 0
    for i in inputs:
        if i == 'you':
            paths += 1
        elif i in output_to_inputs:
            paths += get_paths_to_you(i)
    return paths

@lru_cache(maxsize=None)   # Memoization with unlimited cache
def get_paths_to_svr(key, has_dac, has_fft):
    inputs = output_to_inputs[key]
    paths = 0
    for i in inputs:
        if i == 'svr' and has_fft and has_dac:
            paths += 1
        elif i == 'svr':
            return 0
        elif i in output_to_inputs:
            if i == 'dac':
                paths += get_paths_to_svr(i, True, has_fft)
            elif i == 'fft':
                paths += get_paths_to_svr(i, has_dac, True)
            else:
                paths += get_paths_to_svr(i, has_dac, has_fft)
    return paths

print('Number of paths for part 1: ' + str(get_paths_to_you('out')))

print('Number of paths for part 2: ' + str(get_paths_to_svr('out', False, False)))