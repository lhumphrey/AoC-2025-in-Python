from enum import Enum
from sortedcontainers import SortedKeyList


def area(x1, x2):
    return (abs(x1[0] - x2[0]) + 1) * (abs(x1[1] - x2[1]) + 1)


class Dir(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Orientation(Enum):
    VERTICAL = 1
    HORIZONTAL = 2


class Vertex:
    def __init__(self,pos):
        self.x = pos[0]
        self.y = pos[1]
        self.allowed_directions = []
    
    def set_allowed_directions(self,previous_vertex,next_vertex):
        self.allowed_directions = []
        if previous_vertex.y > self.y:  # Going up
            if next_vertex.x < self.x:  # Going left
                self.allowed_directions = [Dir.UP, Dir.DOWN, Dir.LEFT, Dir.RIGHT]
            elif next_vertex.x > self.x: # Going right
                self.allowed_directions = [Dir.DOWN, Dir.RIGHT]
            else:
                raise Exception("Ill-formatted inputs")
        if previous_vertex.y < self.y: # Going down
            if next_vertex.x < self.x:  # Going left
                self.allowed_directions = [Dir.UP, Dir.LEFT]
            elif next_vertex.x > self.x: # Going right
                self.allowed_directions = [Dir.UP, Dir.DOWN, Dir.LEFT, Dir.RIGHT]
            else:
                raise Exception("Ill-formatted inputs")
        if previous_vertex.x < self.x:  # Going right
            if next_vertex.y > self.y:  # Going down
                self.allowed_directions = [Dir.DOWN, Dir.LEFT]
            elif next_vertex.y < self.y: # Going up
                self.allowed_directions = [Dir.UP, Dir.DOWN, Dir.LEFT, Dir.RIGHT]
            else:
                raise Exception("Ill-formatted inputs")
        if previous_vertex.x > self.x: # Going left
            if next_vertex.y > self.y:  # Going down
                self.allowed_directions = [Dir.UP, Dir.DOWN, Dir.LEFT, Dir.RIGHT]
            elif next_vertex.y < self.y: # Going up
                self.allowed_directions = [Dir.UP, Dir.RIGHT]
            else:
                raise Exception("Ill-formatted inputs")
    
    def get_direction_to(self,v):
        '''Direction from vertex self to vertex v'''
        return Dir.DOWN if self.y < v.y else \
            (Dir.UP if self.y > v.y else \
             (Dir.RIGHT if self.x < v.x else \
               Dir.LEFT))
    
    def to_string(self):
        return 'x:' + str(self.x) + ' y:' + str(self.y) + ', allowed_dir: ' + str(self.allowed_directions)


class LineSegment:
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2
        self.dir = v1.get_direction_to(v2)
    
    def to_string(self):
        return self.v1.to_string() + ', ' + self.v2.to_string() + ', ' + str(self.dir)
    
    def orientation(self):
        return Orientation.VERTICAL if self.dir == Dir.UP or self.dir == Dir.DOWN \
            else Orientation.HORIZONTAL
    
    def crosses(self, ls):
        if self.orientation() == ls.orientation():
            return False
        if self.orientation() == Orientation.VERTICAL:
            if self.v1.y < ls.v1.y < self.v2.y or \
                    self.v1.y > ls.v1.y > self.v2.y:
                if ls.v1.x < self.v2.x < ls.v2.x or \
                    ls.v1.x > self.v2.x > ls.v2.x:
                    return True
        if self.orientation() == Orientation.HORIZONTAL:
            if self.v1.x < ls.v1.x < self.v2.x or \
                    self.v1.x > ls.v1.x > self.v2.x:
                if ls.v1.y < self.v2.y < ls.v2.y or \
                    ls.v1.y > self.v2.y > ls.v2.y:
                    return True
        return False
    
    def runs_over(self, ls):
        if self.orientation() != ls.orientation():
            return False
        if self.orientation() == Orientation.VERTICAL:
            if self.v1.x != ls.v1.x:
                return False
            if self.dir == Dir.UP: # v1.y > v2.y
                if self.v2.y < ls.v1.y <= self.v1.y and not Dir.UP in ls.v1.allowed_directions:
                    return True
                if self.v2.y < ls.v2.y <= self.v1.y and not Dir.UP in ls.v2.allowed_directions:
                    return True
            if self.dir == Dir.DOWN: # v1.y < v1.y
                if self.v1.y <= ls.v1.y < self.v2.y and not Dir.DOWN in ls.v1.allowed_directions:
                    return True
                if self.v1.y <= ls.v2.y < self.v2.y and not Dir.DOWN in ls.v2.allowed_directions:
                    return True
        if self.orientation() == Orientation.HORIZONTAL:
            if self.v1.y != ls.v1.y:
                return False
            if self.dir == Dir.LEFT: # v1.x < v2.x
                if self.v1.x <= ls.v1.x < self.v2.x and not Dir.LEFT in ls.v1.allowed_directions:
                    return True
                if self.v1.x <= ls.v2.x < self.v2.x and not Dir.LEFT in ls.v2.allowed_directions:
                    return True
            if self.dir == Dir.RIGHT: # v1.x > v2.x
                if self.v2.x < ls.v1.x <= self.v1.x and not Dir.RIGHT in ls.v1.allowed_directions:
                    return True
                if self.v2.x < ls.v2.x <= self.v1.x and not Dir.RIGHT in ls.v2.allowed_directions:
                    return True
        return False


def vertex_from_polygon_idx(idx, corner_locs):
    v = Vertex(corner_locs[idx])
    v_prev = Vertex(corner_locs[(idx - 1) % len(corner_locs)])
    v_next = Vertex(corner_locs[(idx + 1) % len(corner_locs)])
    v.set_allowed_directions(v_prev, v_next)
    return v


def goes_outside(seg, line_segments):
    for ls in line_segments:
        if seg.crosses(ls) or seg.runs_over(ls):
            return True


# Main logic
with open('input.txt', 'r') as file:
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

vertices = []
for i in range(len(corner_locs)):
    v = vertex_from_polygon_idx(i, corner_locs)
    vertices.append(v)

lines = []
for i in range(len(vertices) - 1):
    lines.append(LineSegment(vertices[i], vertices[i + 1]))

lines.append(LineSegment(vertices[-1], vertices[0]))

for cp in corner_pairs:
    idx1 = corner_locs.index(cp[0])
    v1 = vertex_from_polygon_idx(idx1, corner_locs)
    idx2 = corner_locs.index(cp[1])
    v2 = vertex_from_polygon_idx(idx2, corner_locs)
    v12 = Vertex([v1.x,v2.y])
    v21 = Vertex([v2.x,v1.y])

    if v1.get_direction_to(v12) not in v1.allowed_directions:
        continue
    if v1.get_direction_to(v21) not in v1.allowed_directions:
        continue
    if v2.get_direction_to(v12) not in v2.allowed_directions:
        continue
    if v2.get_direction_to(v21) not in v2.allowed_directions:
        continue

    v1_to_v12 = LineSegment(v1, v12)
    if goes_outside(v1_to_v12, lines):
        continue
    v1_to_v21 = LineSegment(v1, v21)
    if goes_outside(v1_to_v21, lines):
        continue
    v2_to_v12 = LineSegment(v2, v12)
    if goes_outside(v2_to_v12, lines):
        continue
    v2_to_v21 = LineSegment(v2, v21)
    if goes_outside(v2_to_v21, lines):
        continue
    
    break

print('The total for part 2 is: ' + str(area(cp[0], cp[1])))