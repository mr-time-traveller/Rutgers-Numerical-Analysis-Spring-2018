import matplotlib.pyplot as plt
import numpy as np
from NaturalSpline import cubic_spline
from DividedDifferences import newtdd


x = [0.9, 1.3, 1.9, 2.1, 2.6, 3.0, 3.9, 4.4, 4.7, 5.0, 6.0, 7.0, 8.0, 9.2, 10.5, 11.3, 11.6, 12.0, 12.6, 13.0, 13.3]
a = [1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.15, 2.05, 2.1, 2.25, 2.3, 2.25, 1.95, 1.4, 0.9, 0.7, 0.6, 0.5, 0.4, 0.25]

a_list,b_list,c_list,d_list = cubic_spline(21,x,a)

dd_list = newtdd(x,a)

n = len(x)

for k in range(n-1):
	print "k = ", k, " a: ", a_list[k], " b: ", b_list[k], " c: ", c_list[k], " d: ", d_list[k]

for h in range(len(dd_list)):
	print "F%i,%i = %f " % (h,h, dd_list[h])

def func_s(xn):
	j = 0
	while j < n - 1:
		if xn > x[j] and xn <= x[j+1]:
			return a_list[j]+b_list[j]*(xn-x[j])+c_list[j]*(xn-x[j])**2+d_list[j]*(xn-x[j])**3
		j = j + 1	


def func_pn(xn):
	# get F00
	result = dd_list[0]
	
	for i in range(1,n):
		temp = dd_list[i]
		for j in range(0, i):
			temp = temp*(xn-x[j])
		result = result + temp
	return result



vfun = np.vectorize(func_s)

w = np.linspace(0.9,13.3,30000)
z = vfun(w)
plt.axis([0,14,-2,7])
plt.plot(x, a, 'ro')
plt.plot(w,z,'r-',label='Natural Cubic')

vfun1 = np.vectorize(func_pn)

w1 = np.linspace(0.9,13.3,30000)
z1 = vfun1(w1)
plt.axis([0,14,-2,7])
plt.plot(w1,z1,'b-',label='Newton')
plt.legend()

plt.show()


