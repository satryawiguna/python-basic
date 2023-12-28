myListInteger = [1, 2, 3]
print(myListInteger)

myListString = ['Satrya', 'Wiguna', 'Erna', 'Widhiastuti']
print(myListString)

print(len(myListString))

print(myListString[0])

print(myListString[:2])

print(myListString[2:])

myListInteger[0] = 'Kaela'

print(myListInteger)

myListInteger.append(0)

print(myListInteger)

myListExtend = ['Ganjar', 'Pranowo']

myListInteger.extend(myListExtend)

print(myListInteger)

mySecondList = ['a', 'b', 'c', 'd', 'e']
# item = mySecondList.pop()
item = mySecondList.pop(0)

print(mySecondList)
print(item)

myThirdList = mySecondList
myThirdList.reverse()
print(myThirdList)

myFourthList = [2, 5, 4, 10, 9]
myFourthList.sort()
print(myFourthList)

myFifthList = [1, 2, ['a','b','c']]
print(myFifthList[2][0])

# List Comprehension
myMatrix = [[1,2,3],[4,5,6],[7,8,9]]
fisrtCol = [row[0] for row in myMatrix]
print(fisrtCol)