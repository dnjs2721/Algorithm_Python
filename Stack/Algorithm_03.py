import sys
n = int(sys.stdin.readline().strip())
x = [int(sys.stdin.readline().strip())for _ in range(n)]
count = 1
stack = []
result = []
flag = False

for i in x:
    while count <= i:
        stack.append(count)
        result.append('+')
        count +=1

    if stack[-1] == i:
        stack.pop()
        result.append('-') 
    else:
        flag = True
        break

if flag == False:
    for j in result:
        print(j)
else:
    print("NO")