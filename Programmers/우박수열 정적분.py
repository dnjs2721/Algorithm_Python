def solution(k, ranges):
    answer = []
    arr = [0.0]
    
    while k != 1:
        if k % 2 == 1:
            newk = k * 3 + 1
        else:
            newk = k // 2
        minY, maxY = min(k, newk), max(k, newk)
        arr.append(arr[-1] + (minY + (1/2) * (maxY - minY)))
        k = newk
    
    n = len(arr)
    for x, y in ranges:
        ny = n + y - 1
        if x <= ny:
            answer.append(arr[y-1] - arr[x])
        else:
            answer.append(-1)
            
    return answer

print(solution(5,[[0,0],[0,-1],[2,-3],[3,-3]] ))