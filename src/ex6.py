import re

light_on = {}

for i in range(0, 1000):
    for j in range(0, 1000):
        light_on[(i, j)] = "off"

with open("inputs/input6.txt") as f:
    for line in f:
        print(line, end='')
        numbers = list(re.findall(r'\d+', line))
        if line[0:6] == "toggle":
            for i in range(int(numbers[0]), int(numbers[2]) + 1):
                for j in range(int(numbers[1]), int(numbers[3]) + 1):
                    if (i, j) in light_on.keys() and light_on[(i, j)] == "on":
                        light_on[(i, j)] = "off"
                    else:
                        light_on[(i, j)] = "on"
        else:
            if line[5:7] == "on":
                for i in range(int(numbers[0]), int(numbers[2]) + 1):
                    for j in range(int(numbers[1]), int(numbers[3]) + 1):
                        light_on[(i, j)] = "on"
            else:
                for i in range(int(numbers[0]), int(numbers[2]) + 1):
                    for j in range(int(numbers[1]), int(numbers[3]) + 1):
                        light_on[(i, j)] = "off"

cpt = 0
for key in light_on.keys():
    if light_on[key] == "on":
        cpt += 1

print("Result :", cpt) # Not 673717
