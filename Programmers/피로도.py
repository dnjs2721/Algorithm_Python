# # 순열
# # 몇 개를 골라 순서를 고려해 나열한 경우의 수를 말한다.
# from itertools import permutations
# def solution(k, dungeons):
#     answer = 0
#     for p in permutations(dungeons, len(dungeons)):
#         tmp = k
#         cnt = 0
#         for need, spend in p:
#             if tmp >= need:
#                 tmp -= spend
#                 cnt += 1
#         answer = max(answer, cnt)
#     return answer

# dfs
answer = 0
def dfs(k, cnt, dungeons, visited):
    global answer
    answer = max(answer, cnt)

    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k - dungeons[i][1], cnt + 1, dungeons, visited)
            visited[i] = False

def solution(k, dungeons):
    global answer
    visited = [False] * len(dungeons)
    dfs(k, 0, dungeons, visited)
    return answer

print(solution(80, [[80, 20], [50, 40], [30, 10]]))