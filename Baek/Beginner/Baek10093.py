a, b = map(int, input().split())
res = []
Min = min(a,b)
Max = max(a, b)
if Max - Min == 1:
    print(0)
else:
    for i in range(Min+1, Max, 1):
        res.append(i)
    print(len(res))
    print(*sorted(res))