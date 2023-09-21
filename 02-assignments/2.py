#Write a Python program to multiply all the items in a list

nums = []
print("Enter 5 Numbers: ")
for i in range(5):
  nums.append(int(input()))
mul = 1
for i in range(5):
  mul = mul*nums[i]
print("\nMultiplication Result: ")
print(mul)

