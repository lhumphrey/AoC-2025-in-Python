def is_valid_index(grid, i, j):
    return 0 <= i < len(grid) and \
           0 <= j < len(grid[0])


def num_adjacent_rolls(grid, row, col):
    count = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if is_valid_index(grid, i, j) and not (i == row and j == col):
                if grid[i][j] == 1:
                    count += 1
    return count


# Main logic
grid = []
with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]
for line in lines:
    grid.append([1 if e == '@' else 0 for e in line])

count1 = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 1 and num_adjacent_rolls(grid, i, j) < 4:
            count1 += 1
print('The total for part 1 is: ' + str(count1))

count2 = 0
grid_copy = grid
grid_changed = True
while grid_changed:
    grid = grid_copy
    grid_changed = False
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and num_adjacent_rolls(grid, i, j) < 4:
                grid_copy[i][j] = 0
                grid_changed = True
                count2 += 1

print('The total for part 2 is: ' + str(count2))