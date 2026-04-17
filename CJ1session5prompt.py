#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 15:10:05 2026

@author: maddyjanebronson
"""

import numpy as np
from astropy.table import Table

def main():
    pi = np.pi
        
    x = [0, 2*pi]
    a = np.array(x)
        
    sinx = np.sin(x)
    count = 0
    
    while True:
        sinx = sinx * np.random.random()
        a = a*np.random.random()
        print(sinx, a)
        count = count + 1
        if count > 1000:
            break


#print(sinx)
#print(x)
np.array(Table)

if __name__ == "__main__":
    main()