def parse_fresh_ranges(lines):
    ind = 0
    fresh_ranges = []
    while(lines[ind].find('-') > -1):
        fresh_ranges.append([int(e) for e in lines[ind].split('-')])
        ind += 1
    ind += 1
    return fresh_ranges, lines[ind:]


def get_non_overlapping_next_ranges(base_range, next_range):
    # next_range is strictly less than or greater than base_range
    if next_range[1] < base_range[0] or next_range[0] > base_range[1]:
        return next_range
    # next_range is entirely contained within base_range
    if base_range[0] <= next_range[0] <= base_range[1] \
        and base_range[0] <= next_range[1] <= base_range[1]:
        return []
    # base_range is entirely contained within next_range
    if next_range[0] <= base_range[0] <= next_range[1] \
        and next_range[0] <= base_range[1] <= next_range[1]:
        result = []
        if next_range[0] < base_range[0]:
            result.append([next_range[0], base_range[0] - 1])
        if base_range[1] < next_range[1]:
            result.append([base_range[1] + 1, next_range[1]])
        if len(result) == 1:
            return result[0]
        return result
    # next_range overlaps on base_range's left
    if next_range[0] <= base_range[0] <= next_range[1]:
        return [next_range[0], base_range[0] - 1]
    # next_range overlaps base_range on base_range's right
    if next_range[0] <= base_range[1] <= next_range[1]:
        return [base_range[1] + 1, next_range[1]]
    # Throw an exception for debuggin in case the logic above is wrong
    raise Exception('Unreachable')


def make_fresh_ranges_non_overlapping(ranges):
    base_ind = 0
    fresh_ranges = ranges
    while base_ind < len(fresh_ranges) - 1:
        next_ind = base_ind + 1
        while next_ind < len(fresh_ranges):
            ranges = get_non_overlapping_next_ranges(fresh_ranges[base_ind], fresh_ranges[next_ind])
            if len(ranges) == 0:
                del fresh_ranges[next_ind]
            elif not isinstance(ranges[0], list):
                fresh_ranges[next_ind] = ranges
                next_ind += 1
            elif isinstance(ranges[0], list):
                fresh_ranges[next_ind] = ranges[0]
                fresh_ranges.insert(next_ind,ranges[1])
                next_ind += 2
        base_ind += 1
    return fresh_ranges


def in_a_fresh_range(fresh_ranges, val):
    for range in fresh_ranges:
        if range[0] <= val <= range[1]:
            return True
    return False


# Main logic
with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]
[fresh_ranges, remaining_lines] = parse_fresh_ranges(lines)

count1 = 0
for val in [int(e) for e in remaining_lines]:
    if in_a_fresh_range(fresh_ranges, val):
        count1 += 1
print('The total for part 1 is: ' + str(count1))

count2 = 0
fresh_ranges = make_fresh_ranges_non_overlapping(fresh_ranges)
for interval in fresh_ranges:
    count2 += interval[1] - interval[0] + 1
print('The total for part 2 is: ' + str(count2))