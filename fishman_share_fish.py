# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 13:14:33 2016

@author: 
"""
import numpy as np

a = np.array([1,1,1])
b = np.array([1,0.5,0])

#print (a*b)
c = a*b
d = np.dot(a,b)
#print(sum(c))
#print(d)

weight = [1,0.5,0]
sol = []

for i in range(1,4):
    for j in range(1,4):
        temp = []
        fish_a = [i, 7-i-i, i]
        fish_b = [j, 7-j-j, j]
        fish_c = [7-i-j, 2*i+2*j-7,7-i-j]
        if np.dot(weight, fish_a) == 3.5 and np.dot(weight, fish_b) == 3.5 and fish_c[0] >=0 and fish_c[1] >0:
            temp.append(fish_a)
            temp.append(fish_b)
            temp.append(fish_c)
            sol.append(temp)
            
print("第一組解")
print(sol[0])

print("第二組解")
print(sol[1])
