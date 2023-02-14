import sys

arr =  sys.stdin.readline().rstrip()
stack  = []
stick = 0

for i in range(len(arr)):
    if arr[i] == '(':
        stack.append('(')
    else:
        if arr[i-1] == '(':
            stack.pop()
            stick += len(stack)
        else:
            stack.pop()
            stick += 1

print(stick)