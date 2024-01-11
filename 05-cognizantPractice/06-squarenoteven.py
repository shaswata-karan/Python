# Print square of numbers between 1 to 5 EXCEPT even number
for i in range(1,6):
    if(i%2 == 0):
        continue
    print(i*i)