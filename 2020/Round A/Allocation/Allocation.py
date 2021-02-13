#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def amount(arr, limit):
    arr = sorted(arr)
    count = 0
    temp = 0
    for i in range(len(arr)):
        if arr[i]+temp <= limit:
            temp += arr[i]
            count += 1
    return count
    
import sys
nums = sys.stdin.readlines()

matrix = [[int(num) for num in line.split()] for line in nums]
matrix = matrix[1:]
cases = 0
i = 0 

while i < len(matrix):
    temp =[]
    for k in range(i, i+2):
        temp.append(matrix[k])
    limit = temp[0][1]
    arr = temp[1]
    cases += 1
    print("Case #"+str(cases)+": "+str(amount(arr, limit)))
    i += 2

