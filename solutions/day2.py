from typing import List, Iterator
from aocd import submit, get_data

def is_secure(l: List) -> bool:
    side = 0
    for i in range(len(l) -1):
        diff = l[i+1] - l[i]
        if not 0 < abs(diff) <= 3:
            return False
        if diff > 0 and side == 1:
            return False
        elif diff > 0:
            side = -1
        if diff < 0 and side == -1:
            return False
        elif diff < 0:
            side = 1
    return True

def parse(ipt:str= get_data(day=2,year=2024)) -> Iterator:
    for lines in ipt.split("\n"):
        yield list(map(int, lines.split()))

# ! part 1
submit(sum(is_secure(i) for i in parse()), part="a", day=2, year=2024)

# ! part 2
submit(sum(is_secure(scores) or any(is_secure(scores[0:i] + scores[i+1:len(scores)]) for i in range(len(scores))) for scores in parse()) , part="b", day=2, year=2024)
