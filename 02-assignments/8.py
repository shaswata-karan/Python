#Write a Python program to clone or copy a list

def Cloning(li1):
    li_copy = list(li1)
    return li_copy

li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)