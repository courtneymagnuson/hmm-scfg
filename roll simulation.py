# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 11:18:56 2024

@author: cmag1
"""

import numpy as np
import random

die = 0

S = ''
R = ''

fair = [1,2,3,4,5,6]
loaded = [1,2,3,4,5,6,6,6,6,6]

#i = 0


for i in range(10):
    
    if i == 0:
        num = random.random()
        
        if num < 0.5:
            S = S + "F"
            roll = random.choice(fair)
            R = R + str(roll)
            
        if num >= 0.5:
            S = S + "L"
            roll = random.choice(loaded)
            R = R + str(roll)
            
    if i != 0:
        num = random.random()
        if S[-1] == "F":
            
            if num < 0.95:
                S = S + "F"
                roll = random.choice(fair)
                R = R + str(roll)
                
            if num >= 0.95:
                S = S + "L"
                roll = random.choice(loaded)
                R = R + str(roll)
                
        if S[-1] == "L":
            if num < 0.9:
                S = S + "F"
                roll = random.choice(fair)
                R = R + str(roll)
                
            if num >= 0.9:
                S = S + "L"
                roll = random.choice(loaded)
                R = R + str(roll)
                
    #i = i+1
        
        