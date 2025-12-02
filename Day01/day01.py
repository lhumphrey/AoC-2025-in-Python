with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]

position = 50
count1 = 0
for l in lines:
    dist = int(l[1:])
    dir = l[0]
    if dir == 'R':
        position = (position + dist) % 100
    else:
        position = (position - dist) % 100
    if position == 0:
        count1 += 1

print('The count for part 1 is: ' + str(count1))

position = 50
count2 = 0
for l in lines:
    dist = int(l[1:])
    dir = l[0]
    count2 += int(dist/100)
    rem = dist % 100
    if dir == 'R':
        if position + rem >= 100:
             count2 += 1
        position = (position + dist) % 100
    else:
        if position != 0 and position - rem <= 0:
            count2 += 1
        position = (position - dist) % 100

print('The count for part 2 is: ' + str(count2))