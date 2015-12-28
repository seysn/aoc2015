#!/bin/python
import re

with open("inputs/input12.txt") as f:
    print(sum(int(n) for n in re.findall(r"-?\d+", f.read()))) # 111754
