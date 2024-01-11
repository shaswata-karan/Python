# print monthly expense
# exp = [100, 200, 300, 400, 500]
# # total = exp[0] + exp[1] + exp[2] + exp[3] + exp[4]

# total = 0
# for item in exp:
#     total = total + item

# print("Total expense:",total)


# print month number with expense and then print total amount
exp = [100, 200, 300, 400, 500]
total = 0

for i in range(len(exp)):
    print("Month", (i+1), "Expense:",exp[i])
    total = total + exp[i]
    
print("Total expense:",total)