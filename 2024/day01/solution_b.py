numberList= open("input.txt")
leftList = list()
rightList = list()
index = 0
similarityValue = 0
similarityScore = 0

for line in numberList:
    splitNumbers = line.split("   ")
    leftList.append(int(splitNumbers[0]))
    rightList.append(int(splitNumbers[1]))

leftList = sorted(leftList)
rightList = sorted(rightList)

for item in leftList:
    