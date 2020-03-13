import math
import matplotlib.pyplot as plt
import numpy as np

def linear(n):
	a = []
	for i in n:	
		a.append(i)
	return a
def linearithmic(n):
	a = []
	for i in n:
		b = i * math.log(i)
		a.append(b)
	return a
def logarithmic(n):
	a = []
	for i in n:
		b = i * math.log(i)
		a.append(b)
	return a
def quadratic(n):
	a = []
	for i in n:
		b = pow(i,2)
		a.append(b)
	return a
def exponential(n):
	a = []
	for i in n:
		b = pow(2,i)
		a.append(b)
	return a
def cubic(n):
	a = []
	for i in n:
		b = pow(i,3)
		a.append(b)
	return a
def display():
	value = int(input("Enter a number not greater than 1000:"))
	if value > 1000:
		raise Exception("Stack overflow...")
	
	t = np.arange(1,value,5)
	print(t)
	plt.ylim([-100,2000])
	plt.xlim([-100,250])

	plt.plot(t,linear(t), label = 'Linear')
	plt.plot(t,linearithmic(t), label = 'Linearithmic')
	plt.plot(t,cubic(t), label = 'Cubic')
	plt.plot(t,logarithmic(t), label = 'Logarithmic')
	plt.plot(t,quadratic(t), label = 'Quadratic')
	plt.plot(t,exponential(t), label = 'Exponential')
	# plt.plot(t,linear(t),t,linearithmic(t),t,cubic(t),t,logarithmic(t),t,quadratic(t),t,exponential(t))

	plt.legend()
	plt.xlabel("Rate of Growth")
	plt.ylabel("Values")

	plt.show()

display()

