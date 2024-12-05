from aocd import submit, get_data
import re
import collections
from typing import List, Iterator, Dict

print("DAY 5")


smlthan = {i: [] for i in range(101)}
lgthan = {i: [] for i in range(101)}
listings =[]

def parse(ipt = get_data(day=5, year=2024)):
    for lines in ipt.split("\n"):
        if "|" in lines:
            first, second = tuple(int(i) for i in lines.split("|"))
            lgthan[first].append(int(second))
            smlthan[second].append(int(first))
        if "," in lines:
            listings.append([int(i) for i in lines.split(",")])
        
data = parse()

def check(line: List):
    for i in range(len(line)):
        for sml in smlthan[line[i]]:
            if sml in line:
                if line.index(sml) > i:
                    return False
    return True
#! part 1
p1 = 0
for lines in listings:
    if check(lines):
        p1 += lines[len(lines) // 2]
submit(p1, "a", 5,2024)

# ? qsort from scratch lmfao
def reorder(line):
    if len(line) <= 1:
        return line
    smaller = []
    larger = []
    for i in line:
        smaller = [k for k in smlthan[i] if k in line]
        larger = [k for k in lgthan[i] if k in line]
        if len(smaller) + len(larger) + 1 == len(line):
            pivot = i
            break
    return reorder(smaller) + [pivot] + reorder(larger)

#! part 2

p2 = 0
for lines in listings:
    if not check(lines):
        p2 += reorder(lines)[len(lines)//2]
submit(p2,"b", day=5,year=2024)
