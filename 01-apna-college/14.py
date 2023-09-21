#operations

marks = [20, 30, 50]
marks.append(25)
print(marks)

marks = [20, 30, 50]
marks.insert(1, 25)
print(marks)
print(30 in marks)
print(35 in marks)
print(len(marks))

i = 0
while i < len(marks):
   print(marks[i])
   print(marks[i+1])
   i = i + 2

marks.clear()
print(marks)