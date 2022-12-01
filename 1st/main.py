
import re
inpute_date = open("1st/input.txt")
inpute_date = inpute_date.readlines()
inpute_date = [i.strip() for i in inpute_date]

print(inpute_date)

cals_elfs = []

current_cals = 0
for i in inpute_date:
    if i == "":
        cals_elfs.append(current_cals)
        current_cals = 0
    else:
        current_cals += int(i)

sortedarray = sorted(cals_elfs)

print(cals_elfs)
print()
print()
print(sortedarray)