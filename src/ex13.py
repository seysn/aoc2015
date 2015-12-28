#!/bin/python
from itertools import permutations

def initialize(familly, file):
    for line in file:
        line = line[:-2].split(' ')
        if line[0] not in familly.keys():
            familly[line[0]] = {}
        if line[2] == "gain":
            familly[line[0]][line[-1]] = int(line[3])
        else:
            familly[line[0]][line[-1]] = int('-' + line[3])

def execute(familly):
    optimal = None
    for people in permutations(familly.keys()):
        tmp = 0
        for i in range(-1, len(people) - 1):
            tmp += familly[people[i]][people[i + 1]]
            tmp += familly[people[i + 1]][people[i]]
        if optimal is None or optimal < tmp:
            optimal = tmp
    return optimal

if __name__ == "__main__":
    familly = {}
    with open("inputs/input13.txt") as f:
        initialize(familly, f)
    print(execute(familly))
