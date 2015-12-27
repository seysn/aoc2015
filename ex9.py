#!/bin/python
from itertools import permutations

locations = []
distances = {}

def initialize(locations):
    with open("inputs/input9.txt") as f:
        for line in f:
            line = line.split()
            distances[(line[0], line[2])] = int(line[4])
            distances[(line[2], line[0])] = int(line[4])
            for key in distances.keys():
                if key[0] not in locations:
                    locations.append(key[0])

def execute(locations):
    min_path = None
    max_path = None
    for locs in permutations(locations):
        tmp = 0
        for i in range(1, len(locs)):
            tmp += distances[(locs[i - 1], locs[i])]
        if min_path == None or min_path > tmp:
            min_path = tmp
        if max_path == None or max_path < tmp:
            max_path = tmp
    return (min_path, max_path)

if __name__ == "__main__":
    initialize(locations)
    # print(distances)
    min, max = execute(locations)
    print("Min:", min, "Max:", max)
