import re

varmap = {}
maxnum = 65535

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

with open("input7.txt") as f:
    for line in f:
        dest = line.split(' ')[-1]
        dest = re.sub('\s+', '', dest)
        # print(dest, end=' ')
        # if dest == 'a' or dest == "lx":
        #     print(line)

        if "NOT" in line:
            key = line.split(' ')[1]
            if key in varmap.keys():
                varmap[dest] = varmap[key] ^ maxnum
            else:
                varmap[dest] = maxnum
        elif "OR" in line or "AND" in line:
            key1 = line.split(' ')[0]
            key2 = line.split(' ')[2]
            if key1 not in varmap.keys() and not is_number(key1):
                varmap[key1] = 0
            if key2 not in varmap.keys() and not is_number(key2):
                varmap[key2] = 0

            if "OR" in line:
                if is_number(key1):
                    varmap[dest] = int(key1) | varmap[key2]
                elif is_number(key2):
                    varmap[dest] = varmap[key1] | int(key2)
                else:
                    varmap[dest] = varmap[key1] | varmap[key2]
            else:
                if is_number(key1):
                    varmap[dest] = int(key1) & varmap[key2]
                elif is_number(key2):
                    varmap[dest] = varmap[key1] & int(key2)
                else:
                    varmap[dest] = varmap[key1] & varmap[key2]
        elif "LSHIFT" in line or "RSHIFT" in line:
            key = line.split(' ')[0]
            number = int(line.split(' ')[2])

            if key not in varmap.keys():
                varmap[key] = 0
            if "RSHIFT" in line:
                varmap[dest] = varmap[key] >> number
            else:
                varmap[dest] = varmap[key] << number
        else:
            number = line.split(' ')[0]
            if is_number(number):
                varmap[dest] = int(number)
            else:
                if number not in varmap.keys():
                    varmap[dest] = 0
                else:
                    varmap[dest] = varmap[number]

# for a in sorted(varmap.keys()):
    # if varmap[a] is not 0:
    # print(a, ":", varmap[a])
print("a:", varmap['a'])
