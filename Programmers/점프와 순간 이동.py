# from collections import deque

def solution(n) :
    # visit = [i for i in range(n+1)]
    # q = deque()
    # q.append(1)
    # visit[1] = 1
    # while q:
    #     location = q.popleft()
    #     p = visit[location]
    #     for node in ((location * 2), (location + 1)):
    #         if node > n:
    #             continue
    #         if visit[node] <= p:
    #             continue
    #         if node == location * 2:
    #             if visit[node] > p:
    #                 visit[node] = p
    #         if node == location + 1:
    #             if visit[node] > p:
    #                 visit[node] = p + 1
    #         q.append(node)
    # return visit[n]
    ans = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n -= 1
            ans += 1
    return ans

print(solution(5)) 