import sys

def peaks(matrix):
    count = 0
    i = 1
    while i < len(matrix)-1:
        if (matrix[i-1] < matrix[i]) and (matrix[i+1] < matrix[i]):
            count += 1
        i += 1
    return count

nums = sys.stdin.readlines()
matrix = [[int(num) for num in line.split()] for line in nums]
matrix = matrix[1:]
cases = 0
i = 0 
while i < len(matrix):
    cases += 1
    print("Case #"+str(cases)+": "+str(peaks(matrix[i+1])))
    i += 2
