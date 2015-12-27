instructs = {}
values = {}
maxnum = 65535

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def calculate(arg):
    if arg in values.keys():
        return int(values[arg])

    try:
        return int(arg)
    except ValueError:
        pass
    curr_inst = instructs[arg].split(' ')

    if len(curr_inst) == 1:
        return calculate(curr_inst[0])
    else:
        if curr_inst[0] == "NOT":
            values[arg] = calculate(curr_inst[1]) ^ maxnum
            return values[arg]
        else:
            var1 = curr_inst[0]
            var2 = curr_inst[2]
            try:
                var1 = int(var1)
            except ValueError:
                pass

            try:
                var2 = int(var2)
            except ValueError:
                pass

            if curr_inst[1] == "AND":
                values[arg] = calculate(var1) & calculate(var2)
                return values[arg]
            elif curr_inst[1] == "OR":
                values[arg] = calculate(var1) | calculate(var2)
                return values[arg]
            elif curr_inst[1] == "LSHIFT":
                values[arg] = calculate(var1) << calculate(var2)
                return values[arg]
            else:
                values[arg] = calculate(var1) >> calculate(var2)
                return values[arg]

with open("inputs/input7.txt") as f:
    for line in f:
        tab = line.split(' -> ')
        if len(tab[0].split(' ')) == 1 and is_number(tab[0]):
            values[tab[1][:-1]] = tab[0]
        else:
            instructs[tab[1][:-1]] = tab[0]

if __name__ == "__main__":
    # print(values)
    # print(instructs)
    print("a: ", calculate('a'))
