import sys
    
def kick_start(test_str):
    test_sub = "KICK"
    test_sub2 = "START"
    kicks = 0
    final = 0
    i = 0
    while i < len(test_str):
        if test_str.startswith(test_sub, i):
            kicks +=1
            i += 3
          
        elif test_str.startswith(test_sub2, i):
            final += kicks
            i += 5
  
        else: i += 1
    
    return final
    
content = sys.stdin.readlines()    
content = [x.split() for x in content]
content = content[1:]

for i in range(len(content)):
    print("Case #"+str(i+1)+": "+str(kick_start(content[i][0])))
    

