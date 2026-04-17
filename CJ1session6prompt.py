#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 00:10:01 2026

@author: maddyjanebronson
"""

import numpy as np
from astropy.table import Table
x = [0, 2*np.pi]
def sin(x):
    return np.sin(x)
def cos(x):
    return np.cos(x)
import numpy as np
def main():
    pi = np.pi
        
    x = [0, 2*pi]
    a = np.array(x)
        
    cosx = np.cos(x)
    sinx = np.sin(x)
    count = 0
    
    while True:
        cosx = cosx * np.random.random()
        sinx = sinx * np.random.random()
        a = a*np.random.random()
        print(sinx,cosx, a)
        count = count + 1
        if count > 1000:
            break
np.array(Table)
if __name__ == "__main__":
    main()

def main():
    pi = np.pi
        
    x = [0, 2*pi]
    a = np.array(x)
        
    cosx = np.cos(x)
    sinx = np.sin(x)
    count = 0
    
    while True:
        cosx = cosx * np.random.random()
        sinx = sinx * np.random.random()
        a = a*np.random.random()
        print(sinx,cosx, a)
        count = count + 1
        if count > 10:
            break
np.array(Table)
if __name__ == "__main__":
    main()