# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 11:21:14 2024

@author: cmag1
"""

import numpy as np
import random


sens = []
pos_pred = []

n = 0
j = 0 

while j < 1000:
    
    S = ''
    R = ''

    fair = [1,2,3,4,5,6]
    loaded = [1,2,3,4,5,6,6,6,6,6]

#i = 0


    for i in range(200):
    
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
            
                if num < 0.8:
                    S = S + "F"
                    roll = random.choice(fair)
                    R = R + str(roll)
                
                if num >= 0.8:
                    S = S + "L"
                    roll = random.choice(loaded)
                    R = R + str(roll)
                
            else: 
               if num < 0.3:
                   S = S + "F"
                   roll = random.choice(fair)
                   R = R + str(roll)
                
               if num >= 0.3:
                   S = S + "L"
                   roll = random.choice(loaded)
                   R = R + str(roll)
                



    rolls = R

    trans_mat = [[0.5, 0.5], [0.8, 0.2], [0.3, 0.7]]
    emis_mat = [[1/6, 1/6, 1/6, 1/6, 1/6, 1/6], [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]]

    vF = 0
    vL = 0

    Fdie = trans_mat[1]
    Ldie = trans_mat[2]

    F = emis_mat[0]
    L = emis_mat[1]

    die = 1

    vList = [[], []]

    ## step 1

    vList[0].append(die*trans_mat[0][0]*F[0])
    vList[1].append(die*trans_mat[0][1]*L[0])

    FLlist = [["0"], ["0"]]


## iterate over remaining values

    for i in rolls[1:]:
    
        FF = vList[0][-1]*Fdie[0]*F[int(i)-1]
        FL = vList[0][-1]*Fdie[1]*L[int(i)-1]
    
        LF = vList[1][-1]*Ldie[0]*F[int(i)-1]
        LL = vList[1][-1]*Ldie[1]*L[int(i)-1]
    
        if FF > LF:
            vList[0].append(FF)
            FLlist[0].append("F")
       
        if LF >= FF:
            vList[0].append(LF)
            FLlist[0].append("L")
        
        if FL > LL:
            vList[1].append(FL)
            FLlist[1].append("F")
        
        if LL >= FL:
            vList[1].append(LL)
            FLlist[1].append("L")
        

    guess = ''

    if vList[0][-1] >= vList[1][-1]:
        guess = "F" + guess
    
    if vList[1][-1] > vList[0][-1]:
        guess = "L" + guess
    
    for i in range(1,len(rolls)):
        if guess[0] == 'F':
            guess = str(FLlist[0][-i]) + guess
        
        #if guess[0] == 'L':
        else:
            guess = str(FLlist[1][-i]) + guess
        
        
    nL = S.count("L")
    nLG = guess.count("L")
    
    for i in range(len(rolls)):
        if S[i] == guess[i] and S[i] == "L":
            n = n+1
            
    if nL != 0 and nLG != 0:      
        sens.append(n/nL)
        pos_pred.append(n/nLG)
    
    else:
        sens.append(100)
        pos_pred.append(100)
            
            
#    print("Guess = ", guess)
#    print("Actual = ", S)

        
    n = 0
    
    j = j+1
    
#print("Sensitivity = ", sens)
#print("Positive-Predictive = ", pos_pred)


    

    
