import sys

def robot_path(string):
    N = 0
    W = 0
    E = 0
    S = 0
    tempN = 0
    tempW = 0
    tempS = 0
    tempE = 0
    nums = []
    for elem in string:
        if elem.isdigit():
            nums.append(int(elem))
        elif elem == '(':
            continue
        elif elem == ')':
            nums.pop()
        else:
            if elem == 'N':
                tempN +=1
                for elem in nums:
                    tempN *= elem
                N += tempN
                tempN = 0
            if elem == 'W':
                tempW +=1
                for elem in nums:
                    tempW *= elem
                W += tempW
                tempW = 0
            if elem == 'E':
                tempE +=1
                for elem in nums:
                    tempE *= elem
                E += tempE
                tempE = 0
            if elem == 'S':
                tempS +=1
                for elem in nums:
                    tempS *= elem
                S += tempS
                tempS = 0
    S = S % 1000000000
    N = N % 1000000000
    W = W % 1000000000
    E = E % 1000000000
    result_abs = 1+E-W
    if result_abs <= 0:
        result_abs += 1000000000
    result_ord = 1+S-N
    if result_ord <= 0:
        result_ord += 1000000000   
    return result_abs, result_ord
    
nums = sys.stdin.readlines()
matrix = [line.strip() for line in nums]
matrix = matrix[1:]
cases = 0
i = 0 
while i < len(matrix):
    cases += 1
    print("Case #"+str(cases)+": "+' '.join([str(x) for x in robot_path(matrix[i])]))
    i += 1
