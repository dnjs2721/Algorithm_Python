import sys

while True:
    # 높이를 지정하고 마지막에 0을 삽입
    # 0을 집어넣는 이유 : 마지막에 스택에 있는 값들을 다 꺼내기 위해
    height = list(map(int, sys.stdin.readline().split())) + [0]
    
    if height[0] == 0:
        break
    # 0번째 인덱스의 값은 케이스의 개수   
    n = height[0]
    # 1번째 인덱스의 값
    stack = [(1,height[1])]
    res = 0

    # 1번째 인덱스의 값은 이미 스택에 있으니 2번재 부터 시작
    for i in range(2, n+2):
        width = i
        # 자신보다 스택에 있는 높이가 더 크다면 pop
        while stack and stack[-1][1] > height[i]:
            width, h = stack.pop()
            res = max(res, (i - width) * h)
        stack.append((width,height[i]))

    print(res)