#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 16:25:20 2026

@author: maddyjanebronson
"""

import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

x = np.linspace(0,2*pi,100)

def negative(b):
    if b > 0:
        return -b
    else:
        return b
    

b = 2
a = 5


y = a**(b*x)

plt.rcParams["font.family"] = "Times New Roman"
plt.rc("font", size=14) 

sigma = np.random.normal(10000000)

npoints = 100

scatter = np.random.normal(scale=sigma, size = npoints)

y_new = y + scatter
y_err = np.full(npoints, sigma)

plt.errorbar(x, y_new, yerr=y_err, fmt='o', label='data', c='rebeccapurple')

plt.legend(fontsize=14)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.savefig('CJ2P1',bbox_inches='tight',dpi=600)
