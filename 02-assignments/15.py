#Write a Python program to generate and print a list except for the first 5
#elements, where the values are square of numbers between 1 and 30 (both
#included)
#Enter lower limit : 1
#Enter Upper limit : 30
#[36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256,
#289, 324, 361, 400, 441, 484, 529, 576, 625, 676,
#729, 784, 841]

def printValues():
	l = list()
	for i in range(1,30):
		l.append(i**2)
	print(l[5:])

printValues()