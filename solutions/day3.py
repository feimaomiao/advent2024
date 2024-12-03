import re
from aocd import get_data, submit
txt = get_data(day=3,year=2024)

r = re.compile(r"mul\((\d{1,3})\,(\d{1,3})\)|(do\(\))|(don\'t\(\))")
state = 1
p1 = 0
p2 = 0
for i in r.findall(txt):
    if i[0] and i[1]:
        p1 += int(i[0]) * int(i[1])
        p2 += (int(i[0]) * int(i[1])) * state
    elif i[2]:
        state = 1
    elif i[3]:
        state = 0
print("DAY3")
# ! part 1
submit(p1, part="a", day=3, year=2024)
# ! part 2
submit(p2, part="b", day=3, year=2024)

    

