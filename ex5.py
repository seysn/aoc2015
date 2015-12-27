vowels = ['a', 'e', 'i', 'o', 'u']
bad_str = ["ab", "cd", "pq", "xy"]
nice_str = 0

with open("inputs/input5.txt") as f:
    for line in f:
        boolDoubChar = False
        boolVowels = False
        boolBadStr = False
        if not any(ext in line for ext in bad_str):
            boolBadStr = True

        prevchar = None
        cptvowels = 0
        for c in line:
            if c == prevchar:
                boolDoubChar = True
            prevchar = c
            if c in vowels:
                cptvowels += 1
                if cptvowels == 3:
                    boolVowels = True

        if boolVowels and boolDoubChar and boolBadStr:
            nice_str += 1
            #print(line)

print("Number of nice str :", nice_str)
