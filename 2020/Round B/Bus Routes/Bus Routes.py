#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

def start_day(schedule, target):
    nearest = target-target%schedule[-1]
    for i in range(len(schedule)-1, -1, -1):
        nearest = nearest-nearest%schedule[i]
    return nearest
    
nums = sys.stdin.readlines()
matrix = [[int(num) for num in line.split()] for line in nums]
matrix = matrix[1:]
cases = 0
i = 0 
while i < len(matrix):
    target = matrix[i][1]
    cases += 1
    print("Case #"+str(cases)+": "+str(start_day(matrix[i+1], target)))
    i += 2

