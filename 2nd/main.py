
total_score = 0

rock = ["A","X"]
paper = ["B","Y"]
scissors = ["C","Z"]


data = open("2nd\input.txt")
data = data.read()
data = data.split("\n")

rockamount = 1
paperamount = 2
scissorsamount = 3

for line in data:
    letters = list(line)
    letters.remove(' ')
    print(letters)
    if letters[0] in rock and letters[1] in rock:
        total_score += 3
        total_score += rockamount
    elif letters[0] in paper and letters[1] in paper:
        total_score += 3
        total_score += paperamount
    elif letters[0] in scissors and letters[1] in scissors:
        total_score += 3
        total_score += scissorsamount
    elif letters[0] in rock and letters[1] in paper:
        total_score += 6
        total_score += paperamount
    elif letters[0] in paper and letters[1] in scissors:
        total_score += 6
        total_score += scissorsamount
    elif letters[0] in scissors and letters[1] in rock:
        total_score += 6
        total_score += rockamount
    elif letters[0] in rock and letters[1] in scissors:
        total_score += 0
        total_score += scissorsamount
    elif letters[0] in paper and letters[1] in rock:
        total_score += 0
        total_score += rockamount
    elif letters[0] in scissors and letters[1] in paper:
        total_score += 0
        total_score += paperamount



    

print(total_score)
        

    
