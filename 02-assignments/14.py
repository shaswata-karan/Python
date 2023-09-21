#Write a Python program to generate and print a list of first and last 5
#elements where the values are square of numbers between 1 and 30 (both
#included).
#Enter lower limit : 1
#Enter Upper limit : 30
# [1, 4, 9, 16, 25]
#[625, 676, 729, 784, 841]

def printValues():
	l = list()
	for i in range(1,30):
		l.append(i**2)
	print(l[:5])
	print(l[-5:])

printValues()
