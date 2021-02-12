import sys
nums = sys.stdin.readlines()
matrix = [[int(num) for num in line.split()] for line in nums]
amount = int(matrix[0][0])
nums = matrix[1:]

for i in range(len(nums)):
    print("Case #"+str(i+1)+": "+str(min((nums[i][1]+nums[i][0]), (2*(nums[i][1]-nums[i][2])+nums[i][0]))))
    

