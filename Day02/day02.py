def in_an_id_range(val, id_ranges):
    for id_range in id_ranges:
        if id_ranges[0] <= val <= id_ranges[1]:
            return True
    return False


def is_invalid_1(val):
    val_str = str(val)
    num_digits = len(val_str)
    if num_digits % 2 != 0:
        return False
    if val_str[0:int(num_digits/2)] == val_str[int(num_digits/2):]:
        return True
    return False


def is_invalid_2(val):
    val_str = str(val)
    num_digits = len(val_str)
    if num_digits == 1:
        return False
    divs = []
    divs.append(num_digits)
    for i in range(2, num_digits):
        if num_digits % i == 0:
            divs.append(i)
    for num_substr in divs:
        substr_len = int(num_digits/num_substr)
        first_substr = val_str[0:substr_len]
        status = True
        for i in range(1, num_substr):
            if val_str[i * substr_len:(i + 1) * substr_len] != first_substr:
                status = False
        if status:
            return True
    return False

# Main logic
with open('input.txt', 'r') as file:
    line = file.readline()

id_ranges = []
for entry in line.split(","):
    id_ranges.append([int(i) for i in entry.split("-")])

count1 = 0
for id_range in id_ranges:
    for id in range(id_range[0], id_range[1] + 1):
        if is_invalid_1(id):
            count1 += id
print('The total for part 1 is: ' + str(count1))

count2 = 0
for id_range in id_ranges:
    for id in range(id_range[0], id_range[1] + 1):
        if is_invalid_2(id):
            count2 += id
print('The total for part 2 is: ' + str(count2))