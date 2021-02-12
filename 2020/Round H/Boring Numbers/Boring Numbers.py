#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def boring_number(num):
    amount = -1
    for i in range(len(str(num))):
        amount += 5**i
    nums = [int(d) for d in str(num)]
    length = len(str(num))
    evens = set()
    evens.add(0)
    evens.add(2)
    evens.add(4)
    evens.add(6)
    evens.add(8)
    odds = set()
    odds.add(1)
    odds.add(3)
    odds.add(5)
    odds.add(7)
    odds.add(9)
    for i in range(length):
        count = 0
        left = length-(i+1)
        if i == length-1:
            if (i+1) % 2 == 0:
                for j in evens:
                    if j <= nums[i]:
                        count += 1
            else:
                for k in odds:
                    if k <= nums[i]:
                        count += 1
            
        elif (i+1) % 2 == 0:
            for j in evens:
                if j < nums[i]:
                    count += 1
        else:
            for k in odds:
                if k < nums[i]:
                    count += 1
        amount += count*5**left 
        if (i+1) % 2 == 0 and nums[i] % 2 == 1:
            break
        if (i+1) % 2 == 1 and nums[i] % 2 == 0:
            break
    return amount
    
import sys
nums = sys.stdin.readlines()
matrix = [[int(num) for num in line.split()] for line in nums]
amount = int(matrix[0][0])
matrix = matrix[1:]

for i in range(len(matrix)):
    print("Case #"+str(i+1)+": "+str(boring_number(matrix[i][1])-boring_number(matrix[i][0]-1)))

