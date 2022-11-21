N = int(input())
buildings= [int(input()) for _ in range(N)]
stack = []
res = 0

for i in buildings:
    while stack and stack[-1] <= i: 
        stack.pop()
    stack.append(i) 
    res += len(stack)-1  

print(res)

#10 3 7 4 12 2 일때
# i = 10 일때, 스택이 비어잇기 때문에 스택에 10 추가, stack=[10], res은 0 + len(stack) -1 = 0
# i = 3 일때, 최근 스택(10)이 다음 빌딩(3) 보다 크기 때문에 스택에 3추가, stack=[10, 3], res은 0 + len(stack) -1 = 1
# i = 7 일때, 최근 스택(3)이 다음 빌딩(7) 보다 작기 때문에 pop, stack=[10]
# i = 7 일때, 최근 스택(10)이 다음 빌딩(7) 보다 크기 때문에 스택에 7 추가, stack=[10,7] res은 1 + len(stack) -1 = 2
# i = 4 일때, 최근 스택(7)이 다음 빌딩(4) 보다 크기 때문에 스택에 4 추가, stack=[10,7,4] res은 2 + len(stack) -1 = 4
# i = 12 일때, 최근 스택(4)이 다음 빌딩(12) 보다 작기 때문에 pop, stack=[10,7]
# i = 12 일때, 최근 스택(7)이 다음 빌딩(12) 보다 작기 때문에 pop, stack=[10]
# i = 12 일때, 최근 스택(10)이 다음 빌딩(12) 보다 작기 때문에 pop, stack=[]
# i = 12 일떄, 스택이 비어있기 때문에 스택에 12 추가, stack=[12], res은 4 + len(stack) - 1 = 0
# i = 2 일때, 최근 스택(12)이 다음 빌딩(2) 보다 크기 때문에 스택에 2추가, stac=[12,2], res은 4 + len(stack) -1 = 5
# i = 2 로 for문이 끝났기 때문에 print(res) 출력
# 5