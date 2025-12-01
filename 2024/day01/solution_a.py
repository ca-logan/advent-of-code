numberList= open("input.txt")
leftList = list()
rightList = list()
index = 0
total = 0
difference = 0

for line in numberList:
    splitNumbers = line.split("   ")
    leftList.append(int(splitNumbers[0]))
    rightList.append(int(splitNumbers[1]))

leftList = sorted(leftList)
rightList = sorted(rightList)

while index < len(leftList):
    difference = abs(leftList[index] - rightList[index])
    total += difference
    index += 1

print(total)