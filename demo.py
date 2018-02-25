import math
import matplotlib.pyplot as plt
import numpy as np

def f1(x):
    return 2*math.pow(x,3)-11.7*math.pow(x,2)+17.7*x-5
def f1D(x):
    return 6*math.pow(x, 2)-(2*11.7)*x+17.7
def f2(x):
    return x+10-x*math.cosh(50/x)
def f2D(x):
    return (1+math.sinh(50/x)*(50/x)-math.cosh(50/x))
def approxError(c,p):
    return abs((c-p)/c) if c!=0 else 100000000000

def bisection(f, a, b, maxIterations, epsilon):
    if f(a)*f(b) > 0:
        print('Values of a and b do not bracket the root')
        return
    c = 0
    errors = {}
    for n in range(0,maxIterations):
        prevC = c
        c = (a+b) / 2    
        errors[n] = approxError(c,prevC)
        if errors[n] < epsilon or f(c) == 0:
            return zip(*sorted(errors.items()))
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

def newton(f, fp, x, maxIterations, epsilon, delta):
    errors = {}
    for n in range(0,maxIterations):
        if abs(fp(x)) < delta or abs(fp(x)) == 0:
            print("Derivative approaching zero- cannot find root")
            return
        prevX = x 
        x-= f(x) / fp(x)
        errors[n] = approxError(x,prevX)
        if errors[n] < epsilon or f(x) == 0:
            print(errors)
            return zip(*sorted(errors.items()))

def graphResults():
    pass

print('Enter the desired error: ')
error1 = input()
print('Enter the maximum number of iterations:')
maxIterations = input()

b1iterations,b1error = bisection(f1,-1,1,int(maxIterations),float(error1))
n1iterations,n1error = newton(f1,f1D,.5,int(maxIterations),float(error1),.00001)
plt.figure(1)
plt.subplot(311)
plt.plot(b1iterations[1:],b1error[1:],'b')
plt.plot(n1iterations[1:],n1error[1:],'r')
plt.yscale('log')
plt.xscale('log')

plt.subplot(312)
b2iterations,b2error = bisection(f1,1,2,int(maxIterations),float(error1))
n2iterations,n2error = newton(f1,f1D,2,int(maxIterations),float(error1),.00001)
plt.plot(b2iterations[1:],b2error[1:],'b')
plt.plot(n2iterations[1:],n2error[1:],'r')
plt.yscale('log')
plt.xscale('log')

plt.subplot(313)
b3iterations,b3error = bisection(f1,3,4,int(maxIterations),float(error1))
plt.plot(b3iterations[1:],b3error[1:],'b')
n3iterations,n3error = newton(f1,f1D,3,int(maxIterations),float(error1),.00001)
plt.plot(n3iterations[1:],n3error[1:],'r')
plt.yscale('log')
plt.xscale('log')
plt.show()
