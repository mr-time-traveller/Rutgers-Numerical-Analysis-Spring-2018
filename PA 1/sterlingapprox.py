import math
for i in range(1,11):
    a=math.sqrt(2*math.pi*i)*((i/math.e)**i)
    print ("n=", i, 'absolute error=', abs(a - math.factorial(i)), "relative error=", abs(a - math.factorial(i)) / math.factorial(i))