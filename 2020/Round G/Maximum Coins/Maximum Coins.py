import sys

def diagonal_sum(matrix):
    length = len(matrix[0])
    fin = 0
    temp = 0
    for j in range(length-1, -1, -1):
        i = 0
        while i < length and j < length:
            temp += matrix[i][j]
            i += 1
            j += 1 
        if temp > fin:
            fin = temp
        i = 0
        temp = 0
    for j in range(length-1, -1, -1):
        i = 0
        while i < length and j < length:
            temp += matrix[j][i]
            i += 1
            j += 1 
        if temp > fin:
            fin = temp
        i = 0
        temp = 0
    return fin
    

nums = sys.stdin.readlines()
matrix = [[int(num) for num in line.split()] for line in nums]
matrix = matrix[1:]
i = 0
cases = 0
while i < len(matrix):
    j = matrix[i][0]
    temp =[]
    for k in range(i+1,i+1+j):
        temp.append(matrix[k])
    cases += 1
    if len(temp) > 1:
        print("Case #"+str(cases)+": "+str(diagonal_sum(temp)))
    else:
        print("Case #"+str(cases)+": "+str(temp[0][0]))
    i += j+1
