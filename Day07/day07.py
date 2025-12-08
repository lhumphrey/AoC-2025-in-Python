import re
from functools import reduce

def beam_paths(location, remaining_lines):
    if len(remaining_lines) == 0:
        return 1
    elif remaining_lines[0][location] == '^':
        num_paths = 0
        location_1 = location - 1
        location_2 = location + 1
        if location_1 >= 0:
            num_paths += beam_paths(location_1, remaining_lines[1:])
        if location_2 < len(lines[0]):
            num_paths += beam_paths(location_2, remaining_lines[1:])
        return num_paths
    else:
        return beam_paths(location, remaining_lines[1:])



# Main logic
with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]

count1 = 0
beam_locations = [lines[0].find('S')]
max_ind = len(lines[0]) - 1
for l in lines[1:]:
    splitter_locations = [m.start() for m in re.finditer('\^', l)]
    for split_loc in splitter_locations:
        if split_loc in beam_locations:
            count1 += 1
            ind = beam_locations.index(split_loc)
            new_loc1 = beam_locations[ind] - 1
            new_loc2 = beam_locations[ind] + 1
            del beam_locations[ind]
            if new_loc1 >= 0 and not new_loc1 in beam_locations:
                beam_locations.append(new_loc1)
            if new_loc2 <= max_ind and not new_loc2 in beam_locations:
                beam_locations.append(new_loc2)
print('The total for part 1 is: ' + str(count1))

count2 = 0
beam_locations = [0] * len(lines[0])
start_ind = lines[0].find('S')
beam_locations[start_ind] = 1
max_ind = len(lines[0]) - 1
for l in lines[1:]:
    splitter_locations = [m.start() for m in re.finditer('\^', l)]
    new_beam_locations = [0] * len(lines[0])
    for beam_ind in range(len(beam_locations)):
        if beam_locations[beam_ind] > 0:
            if beam_ind in splitter_locations:
                new_loc1 = beam_ind - 1
                new_loc2 = beam_ind + 1
                if new_loc1 >= 0:
                    new_beam_locations[new_loc1] += beam_locations[beam_ind]
                if new_loc2 <= max_ind:
                    new_beam_locations[new_loc2] += beam_locations[beam_ind]
            else:
                new_beam_locations[beam_ind] += beam_locations[beam_ind]
    beam_locations = new_beam_locations
print('The total for part 2 is: ' + str(sum(beam_locations)))

#beam_locations = [lines[0].find('S')]
#count2 = beam_paths(beam_locations[0], lines[1:])
# print('The total for part 2 is: ' + str(count2))
# 21852865 is too low