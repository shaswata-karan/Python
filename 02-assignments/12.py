#Write a Python program to print the numbers of a specified list after
#removing even numbers from it.
#Enter number of elements : 7
#7
# 8
#120
#25
#44
#20
#27
#[7, 25, 27]

evenList = []

listNumber = int(input("Enter the Total List Items = "))
for i in range(1, listNumber + 1):
    listValue = int(input("Enter the %d List Item = " % i))
    evenList.append(listValue)

print("List Items = ", evenList)
i = 0

while (i < len(evenList)):
    if (evenList[i] % 2 == 0):
        evenList.remove(evenList[i])
    i = i + 1

print("List Items after removing even Items = ", evenList)

