#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def combination_lock(maximum, initial):
    result = math.inf
    temp_sum = 0
    length = len(initial)
    for i in range(length):
        target = initial[i]
        for j in range(i):
            temp = initial[j]
            temp_sum += min(target-temp, maximum - target + temp)
        for j in range(i+1, length):
            temp = initial[j]
            temp_sum += min(temp-target, maximum - temp + target)
        if temp_sum < result:
            result = temp_sum
        temp_sum = 0
    return result
    
import sys
import math
nums = sys.stdin.readlines()


matrix = [[int(num) for num in line.split()] for line in nums]
matrix = matrix[1:]

cases = 0
i = 0 

while i < len(matrix):
    temp =[]
    for k in range(i, i+2):
        temp.append(matrix[k])
    maximum = temp[0][1]
    initial = temp[1]
    initial = sorted(initial)
    cases += 1
    print("Case #"+str(cases)+": "+str(combination_lock(maximum, initial)))
    i += 2

