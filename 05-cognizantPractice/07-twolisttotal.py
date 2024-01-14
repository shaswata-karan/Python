list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [11, 12, 13, 14, 15, 16, 17, 18]

# total = 0
# for item in list1:
#     total=total+item
# print("list1 total:", total)

# total = 0
# for item in list2:
#     total=total+item
# print("list2 total:", total)

def calculate_total(exp):
    total = 0
    for item in exp:
        total=total+item
    return total

list1_total = calculate_total(list1)
list2_total = calculate_total(list2)

print("list1 total:",list1_total)
print("list2 total:",list2_total)