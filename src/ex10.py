#!/bin/python
import re
puzzle_input = "1321131112"

for i in range(40):
    puzzle_input = [m.group(0) for m in re.finditer(r"(\d)\1*", puzzle_input)]
    print(i)
    tmp = str()
    for c in puzzle_input:
        tmp += str(len(c))
        tmp += c[0]
    puzzle_input = tmp

print(len(puzzle_input))
