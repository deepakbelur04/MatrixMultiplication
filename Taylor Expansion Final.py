import sympy as sym
from sympy import Subs, Function
import numpy as np
import math
import matplotlib.pyplot as plt

x = sym.Symbol('x')

yAxis = [ ]
xAxis = [ ]

tyAxis = [ ]

def valueOrigEquation(fX, value):
    diffValue = fX.subs(x, value)
    return diffValue


def taylorExpVal(fX,xvalue,avalue):
    f0 = fX.subs(x, xvalue)
    print(f0)
    sum = f0
    for i in range(1,3):
        equation = sym.diff(fX, x)
        newterm = (equation.subs(x, xvalue)) / math.factorial(i)
        xadiff = (xvalue-avalue)**i
        newterm = newterm * xadiff
        sum += newterm
    return sum


def rangeDefPlot(fX):
    for aval in np.arange(-5,5,0.5):
        min = aval - 0.5
        max = aval + 0.5
        i = 0
        for xval in np.arange(min,max,0.1):
            yAxis.append(valueOrigEquation(fX, xval))
            xAxis.append(xval)
            tyAxis.append(taylorExpVal(fX, xval, aval))

    print("{0},{1}".format(len(tyAxis),len(xAxis)))
    plt.plot(xAxis,yAxis,'blue')
    plt.plot(xAxis,tyAxis,'gray')
    plt.ylabel('DerivativeValue')
    plt.xlabel('X Value')
    plt.show()

fX = x ** 2 /20
rangeDefPlot(fX)