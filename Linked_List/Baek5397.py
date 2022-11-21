import sys
num = int(sys.stdin.readline().rstrip())

for _ in range(num):
    str = list(sys.stdin.readline().rstrip())
    left, right = [], []

    for i in str:
        if i == '<':
            if left != []:
                right.append(left.pop())
        elif i == '>':
            if right != []:
                left.append(right.pop())
        elif i == '-' :
            if left != []:
                left.pop()
        else :
            left.append(i)
    print(''.join(left) + ''.join(list(reversed(right))))