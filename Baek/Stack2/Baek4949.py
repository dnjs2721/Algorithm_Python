import sys

res = []

while True:
    stack = []
    flag = False

    x = sys.stdin.readline().rstrip()
    if x != ".":
        for i in x:
            if i == '(' or i == '[' :
                stack.append(i)
            elif i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    flag = True
                    break
            elif i == ']':
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    flag = True
                    break
        if stack:
            flag = True

        if flag  :
            res.append("no")
        else:
            res.append("yes")      
    else:
        break

for i in res:
    print(i)