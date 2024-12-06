from aocd import submit, get_data
import re
import collections
from typing import List, Iterator, Dict
import copy

print("DAY 6")



directions = {
    -1 :(-1, 0), # ^
    -2 :(0, -1), # <
    -3 :(1,0), # v
    -4 :(0,1) # >

}
direction_list = [(-1,0), (0,1),(1,0),(0,-1)]

mapping = {
    "^": -1,
    "<" : -2,
    "v" : -3,
    ">" :-4
}

def parse(dt = get_data(day=6,year=2024)):
    for k in mapping:
        if k in dt:
            direction = mapping[k]
    
    data = [[1 if k == "#" else -1 for k in i] for i in dt.splitlines()]
    width, height = (len(data[0]), len(data))
    for index, i in enumerate(dt.splitlines()):
        for index2, j in enumerate(i):
            if j in mapping:
                x = index2
                y = index
    return (data, direction ,width, height, x, y)

        

def run(data, direction, width, height, x, y):
    seen = []
    data[y][x] = 0
    ctr = 1
    dy, dx = directions[direction]
    while 0 <= x + dx < width and 0 <= y + dy < height:
        if data[y+dy][x+dx] <= 0:
            y += dy
            x += dx
            if data[y][x] < 0:
                ctr += 1
            data[y][x] = 0
            seen.append((x,y))
        elif data[y + dy][x+dx] == 1:
            dy, dx = direction_list[(direction_list.index((dy,dx)) + 1) % 4]
    return (ctr, seen)
            


data, direction , width, height, x, y= parse()


p1, seen = run(data, direction, width, height, x, y)
submit(p1, part="a", day=6, year=2024)
def run2(data, direction, width, height, x, y):
    hits = set()
    seen = []
    data[y][x] = 0
    ctr = 1
    dy, dx = directions[direction]
    while 0 <= x + dx < width and 0 <= y + dy < height:
        if data[y+dy][x+dx] <= 0:
            y += dy
            x += dx
            if data[y][x] < 0:
                ctr += 1
            data[y][x] = 0
            seen.append((x,y))
        elif data[y + dy][x+dx] == 1:
            if (x+dx, y+dy, x, y ,dx, dy) in hits:
                return True
            hits.add((x +dx, y+dy, x, y,dx,dy))
            dy, dx = direction_list[(direction_list.index((dy,dx)) + 1) % 4]
    return False


def has_neighbor(data, y, x, height, width):
    if data[y][x] == 0:
        return True
    for (dy,dx) in directions.values():
        if not (0<= y + dy <height and 0 <= x + dx < width):
            continue
        if data[y + dy][x + dx] == 0:
            return True
    return False

# print(run2(data, direction, width, height,x,y))
seen = set(seen)
p2 = 0
runs = 0
# if one were to optimize this they would only check the perimeters
for h in range(height):
    for w in range(width):
        if (h,w) == (y,x):
            continue
        if not has_neighbor(data, h,w, height, width):
            continue
        runs += 1
        new_data = copy.deepcopy(data)
        new_data[h][w] =1 
        if run2(new_data, direction, width, height, x, y):
            p2 += 1

submit(p2, part="b", day=6, year=2024)
print(runs)