#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 18:27:16 2026

@author: maddyjanebronson
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(20)

npoints = 50

x = np.linspace(0,10, npoints)

def negative(b):
    if b > 0:
        return -b
    else:
        return b

slope = 5.0
b = 2.0
y_clean = slope*np.exp(negative(b)*x)

#plt.plot(x, y_clean)

#plt.xlabel("x")
#plt.ylabel("y")

sigma = 3
scatter = np.random.normal(scale=sigma, size=npoints)
y_new = y_clean + scatter
y_err = np.full(npoints, sigma)


plt.errorbar(x, y_new, yerr=y_err, fmt='^')
plt.xlabel("x")
plt.ylabel("y (with scatter)")

from scipy.optimize import curve_fit

def model_line1(a, x, b):
    y_model = a*np.exp(negative(b)*x)
    return y_model

def model_line2(a, x, b):
    y_model = a/(x**b)
    return y_model
params1, params_cov1 = curve_fit(model_line1, x, y_new, sigma = y_err, p0=[1,0])
params2, params_cov2 = curve_fit(model_line1, x, y_new, sigma = y_err, p0=[1,0])

a_fit1 = params1[0]
b_fit1 = params1[1]

a_fit2 = params2[0]
b_fit2 = params2[1]
print(f"The true value of the line was a = 5, b = 2. Curve_fit found a= {a_fit1:3.2}, b = {b_fit1:3.2}")

y_fit1 = model_line1(x, a_fit1, b_fit1)
y_fit2 = model_line2(x, a_fit2, b_fit2)
print(f"The true value of the line was a = 5, b = 2. Curve_fit found a= {a_fit2:3.1}, b = {b_fit2:3.1}")

plt.errorbar(x, y_new, yerr=y_err, fmt='^', label='data')
plt.plot(x, y_fit1, label='fit1')
plt.plot(x, y_fit2, label='fit2')
plt.legend(fontsize=13)
plt.xlabel("x")
plt.ylabel("y")
plt.savefig('CJ2P3',bbox_inches='tight',dpi=600)
