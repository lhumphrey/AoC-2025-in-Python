from math import sqrt
from sortedcontainers import SortedKeyList

def area(x1, x2):
    return (abs(x1[0] - x2[0]) + 1) * (abs(x1[1] - x2[1]) + 1)

class Vertex:
    def __init__(self,pos):
        self.x = pos[0]
        self.y = pos[1]
        self.can_go_up = False
        self.can_go_down = False
        self.can_go_left = False
        self.can_go_right = False

    def set_directions(self,previous_vertex,next_vertex):
        if previous_vertex.y > self.y:  # Going up
            if next_vertex.x < self.x:  # Going left
                self.can_go_up, self.can_go_down = True, True
                self.can_go_left, self.can_go_right = True, True
            elif next_vertex.x > self.x: # Going right
                self.can_go_down = True
                self.can_go_right = True
            else:
                raise Exception("Ill-formatted inputs")
        if previous_vertex.y < self.y: # Going down
            if next_vertex.x < self.x:  # Going left
                self.can_go_up, self.can_go_left = True, True
            elif next_vertex.x > self.x: # Going right
                self.can_go_up, self.can_go_down = True, True
                self.can_go_left, self.can_go_right = True, True
            else:
                raise Exception("Ill-formatted inputs")
        if previous_vertex.x < self.x:  # Going right
            if next_vertex.y > self.y:  # Going down
                self.can_go_down = True
                self.can_go_left = True
            elif next_vertex.y < self.y: # Going up
                self.can_go_up, self.can_go_down = True, True
                self.can_go_left, self.can_go_right = True, True
            else:
                raise Exception("Ill-formatted inputs")
        if previous_vertex.x > self.x: # Going left
            if next_vertex.y > self.y:  # Going down
                self.can_go_up, self.can_go_down = True, True
                self.can_go_left, self.can_go_right = True, True
            elif next_vertex.y < self.y: # Going up
                self.can_go_up, self.can_go_right = True, True
            else:
                raise Exception("Ill-formatted inputs")

    def _dir_string(self):
        str = ''
        if self.can_go_up:
            str += ' up '
        if self.can_go_down:
            str += ' down '
        if self.can_go_right:
            str += ' right '
        if self.can_go_left:
            str += ' left '
        return str

    def to_string(self):
        return 'x:' + str(self.x) + ' y:' + str(self.y) + ', dir={' + self._dir_string() + '}'


class LineSegment:
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2


# Main logic
with open('input_ex.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]

corner_locs = []
for line in lines:
    corner_locs.append([int(e) for e in line.split(',')])

corner_pairs = SortedKeyList(key=lambda x: -area(x[0], x[1]))
for i in range(len(corner_locs)):
    for j in range(i + 1,len(corner_locs)):
        corner_pairs.add([corner_locs[i], corner_locs[j]])

count1 = area(corner_pairs[0][0], corner_pairs[0][1])
print('The total for part 1 is: ' + str(count1))
# 4748985168

vertices = []
for i in range(len(corner_locs)):
    v = Vertex(corner_locs[i])
    v_prev = Vertex(corner_locs[(i - 1) % len(corner_locs)])
    v_next = Vertex(corner_locs[(i + 1) % len(corner_locs)])
    v.set_directions(v_prev, v_next)
    vertices.append(v)

for v in vertices:
    print(v.to_string())