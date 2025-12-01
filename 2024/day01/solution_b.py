numberList= open("input.txt")
leftList = list()
rightList = list()
similarityValue = 0
similarityScore = 0

for line in numberList:
    splitNumbers = line.split("   ")
    leftList.append(int(splitNumbers[0]))
    rightList.append(int(splitNumbers[1]))

leftList = sorted(leftList)
rightList = sorted(rightList)

for item in leftList:
    similarityValue = item
    instances = 0
    while rightList.index(item):
        instances += 1
        rightList.remove(item)
    similarityValue *= instances
    similarityScore += similarityValue

print(similarityScore)