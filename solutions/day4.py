from aocd import submit, get_data
import re
import collections
from typing import List, Iterator, Dict

print("DAY4")

def parse(ipt=get_data(day=4, year=2024)):
    return [list(i) for i in ipt.split("\n")]


data = parse()
width = len(data[0])
height = len(data)

expect = ["X", "M", "A", "S"]
perms = [
    (-1,-1), (-1,0), (-1,1), (0,-1), (0,1),(1,-1), (1,0), (1,1)
]
# ? Glorified bfs
def check(data: List[List[str]], y, x):
    ret = 0
    for dx, dy in perms:
        if dx == dy == 0:
            continue
        add = 1
        if not (0 <= x + 3 * dx < width and 0 <= y + 3 * dy < height):
            continue
        for i in range(4):
            if data[y + i * dy][x + i * dx] != expect[i]:
                add = 0
        ret += add
    return ret


#! Part 1
p1 = 0
# find location of X and calling bfs on it 
for y in range(height):
    for x in range(width):
        if data[y][x] == "X":
            p1 += check(data, y,x)


submit(p1, part="a", year=2024, day=4)

combinations2 = [[(-1,-1), (1,1)], [(-1,1), (1,-1)]]

# ? Glorified bfs part 2
expect2 = set(["M","S"])
def check2(data, y, x):
    ret = 0
    ctr = 2
    if any([y-1 < 0, y+1 >= height, x-1 < 0, x+1 >= width]):
        return 0
    for i in combinations2:
        elems = set(data[y + dy][x + dx] for dx, dy in i)
        if elems == expect2:
            ctr -=1
    return int(not ctr)

    
# ! Part 2
    
p2 = 0
for y in range(height):
    for x in range(width):
        if data[y][x] == "A":
            p2 += check2(data, y,x)
        
    
submit(p2, part="b", year=2024, day=4)