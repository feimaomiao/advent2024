from typing import List
import collections
from aocd import submit, get_data

text: str= get_data(day=1,year=2024)
list1 = list(map(lambda x: int(x.split("   ")[0]),text.split("\n")))
list2 = list(map(lambda x: int(x.split("   ")[1]),text.split("\n")))
list1.sort()
list2.sort()
ctr = collections.Counter(list2)
print("DAY 1")
submit(sum(abs(b-a) for a,b in zip(list1, list2)), part="a", year=2024, day=1)
submit(sum(ctr.get(i, 0) * i for i in list1), part="b", year=2024, day=1)
