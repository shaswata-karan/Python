#if - elif - else Statements

age = input("Enter your age: ")
age = int(age)

if age >= 18:
   print("you are an adult")
   print("you can vote")
elif age < 3:
   print("you are a child")
else:
   print("you are in school")

print("thank you")