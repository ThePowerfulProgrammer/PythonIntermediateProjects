# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 15:41:01 2024

@author: ashis
"""

q = [1150,2000, 1212, 2396, 2800, 544, 1618, 346, 1523, 3965, 3681]
q = sorted(q)
print(q)
# Direction is still left
totalCylinderMovement = 0

startingIndex = q.index(1150)

for i in range(startingIndex,0,-1):
    totalCylinderMovement += abs(q[i] - q[i+1])
    
print(totalCylinderMovement)


totalCylinderMovement += 3999 - q[-1]

startingIndex = -2

for i in range(-2,3,1):
    
    totalCylinderMovement += abs(q[i] - q[i-1])
    
print(totalCylinderMovement)