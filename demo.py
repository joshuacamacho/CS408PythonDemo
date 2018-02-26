# CS 408 - Group Project - Python Demo
# Joshua Camacho and Danielle Holzberger
#
# Root approximation using bisection and Newton's method
# with graphic results

import math
import matplotlib.pyplot as plt
import numpy as np

#Function whose roots are to be calculated
def f1(x):
    return 2*math.pow(x,3)-11.7*math.pow(x,2)+17.7*x-5

#Deriviative of the function
def f1D(x):
    return 6*math.pow(x, 2)-(2*11.7)*x+17.7

#Calculates the approximate error between iterations
def approxError(c,p):
    return abs((c-p)/c) if c!=0 else 100000000000

#Determines the root of a function by providing
#values that bracket the root
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
#Determines the root of a function by using
#an initial guess
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
            return zip(*sorted(errors.items()))

print('Enter the desired error: ')
error1 = input()
print('Enter the maximum number of iterations:')
maxIterations = input()

#Comparion of methods for root 1
b1iterations,b1error = bisection(f1,-1,1,int(maxIterations),float(error1))
n1iterations,n1error = newton(f1,f1D,.5,int(maxIterations),float(error1),.00001)
plt.figure(1)
plt.subplot(311)
plt.plot(b1iterations[1:],b1error[1:],'b')
plt.plot(n1iterations[1:],n1error[1:],'r')
plt.yscale('log')
plt.xscale('log')
plt.title('Number of Iterations vs. Approximate Error for Root 1')
plt.xlabel('Number of Iterations')
plt.ylabel('Approximate Error')

#Comparison of methods for root 2
plt.subplot(312)
b2iterations,b2error = bisection(f1,1,2,int(maxIterations),float(error1))
n2iterations,n2error = newton(f1,f1D,1.5,int(maxIterations),float(error1),.00001)
plt.plot(b2iterations[1:],b2error[1:],'b')
plt.plot(n2iterations[1:],n2error[1:],'r')
plt.yscale('log')
plt.xscale('log')
plt.title('Number of Iterations vs. Approximate Error for Root 2')
plt.xlabel('Number of Iterations')
plt.ylabel('Approximate Error')

#Comparison of methods for root 3
plt.subplot(313)
b3iterations,b3error = bisection(f1,3,4,int(maxIterations),float(error1))
plt.plot(b3iterations[1:],b3error[1:],'b')
n3iterations,n3error = newton(f1,f1D,3,int(maxIterations),float(error1),.00001)
plt.plot(n3iterations[1:],n3error[1:],'r')
plt.yscale('log')
plt.xscale('log')
plt.title('Number of Iterations vs. Approximate Error for Root 3')
plt.xlabel('Number of Iterations')
plt.ylabel('Approximate Error')
plt.show()
