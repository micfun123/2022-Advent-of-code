#3rds advent of code 2022

input = open("3rd\inpute.txt")
input = input.readlines()
commonletters = []
totalscore = 0

for i in input:
    #split the string in half
    firsthalf = i[:len(i)//2]
    secondhalf = i[len(i)//2:]
    print(firsthalf)
    print(secondhalf)
    #find common letters
    commonletter = (set(firsthalf) & set(secondhalf)).pop()
    commonletters.append(commonletter)

print(commonletters)
for i in commonletters:
    if i == i.lower():
        totalscore += ord(i) - 96
    else:
        totalscore += ord(i) - 38

print(totalscore)