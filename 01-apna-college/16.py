#tuple
marks = (95, 98, 97, 97)
print(marks.count(97))
print(marks.index(97))

print("--------------------")

#sets
marks = {98, 97, 95, 95}
print(marks)
for score in marks:
   print(score)

print("--------------------")

#dictionary
marks = {"math" : 99, "chemistry" : 98, "physics" : 97}
print(marks)
print(marks["chemistry"])

marks["english"] = 95
print(marks)

marks["math"] = 96
print(marks)
