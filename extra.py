# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 14:00:47 2024

@author: cmag1
"""

rolls = "56445363451264156521622312164363243313666336146536351516533135146254651361361543643414244612256424665433226634334555255536365445464254626166652351636663146266442563564116126665565563533634551213165543"
dice = "FFFFFFFFFFFLLLFFFFFFLLFFLFFFFFFFFFFFFFLLLFFFFFLFFLLFFFFLFFFFFFFFFFFFLFFFFFFFFFLFFFFFFFFFFFFFFFLLFFFFFFFFFFLLLLFFFFFFFLLFFLLFFFFFFFFFFFFFFFLLLLLFFFLFLLLLFFLLLLFFFFLLFFFFFFFLLLLFFFFFFFFFFFFFFFFFFLFFFFFF"
viterbi = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFLLLFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFLLLLLLLFFFFFLLLLLLLLLLLLFFFFFFFFFFFFFFLLLFFFFFFFFFFFFFFFFFFFFFFFFF"

#for i in range(3):
 #   newrolls = rolls[70*i:70*(i+1)]
  #  newdice = dice[70*i:70*(i+1)]
   # newviterbi = viterbi[70*i:70*(i+1)]
    
   # print("Rolls = ", newrolls)
   # print("Dice = ", newdice)
   # print("Viterbi = ", newviterbi)
   # print("-----------------------------------")
    
    
fair = [1,2,3,4,5,6]
loaded = [1,2,3,4,5,6,6,6,6,6]

#i = 0

trans_mat = [[0.5, 0.5], [0.8, 0.2], [0.3, 0.7]]
emis_mat = [[1/6, 1/6, 1/6, 1/6, 1/6, 1/6], [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]]

S = ''

    
#rolls = '56536'
    
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
    
print(rolls)


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
        
        
 
            
print("Guess = ", viterbi)
print("Actual = ", dice)
print("-----------------------------------")

n=0

sens = []
pos_pred = []

nL = dice.count("L")
nLG = viterbi.count("L")
    
for i in range(len(rolls)):
    if dice[i] == viterbi[i] and dice[i] == "L":
            n = n+1
            
if nL != 0 and nLG != 0:      
        sens.append(n/nL)
        pos_pred.append(n/nLG)
    
else:
        sens.append(100)
        pos_pred.append(100)
        
        
print("Sensitivity = ", sens)
print("Positive-Predictive = ", pos_pred)

  