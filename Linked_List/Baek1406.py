import sys
str = list(sys.stdin.readline().rstrip())
num = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(num):
    com = sys.stdin.readline().rstrip().split()
    
    if com[0] == 'L':
        if str != []:
            stack.append(str.pop())
    elif com[0] == 'D' :
        if stack != []:
            str.append(stack.pop())
    elif com[0] == 'B' :
        if str != []:
            str.pop()
    elif com[0] == 'P':
        str.append(com[1])

print(''.join(str)+''.join(list(reversed(stack))))