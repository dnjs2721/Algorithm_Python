# from collections import deque

# def solution(numbers):
#     answer = 0
#     number_pad = [['1','2','3'],['4','5','6'],['7','8','9'],['*','0','#']]
    
#     dx = [1, -1, 0, 0, 1, -1, 1, -1]
#     dy = [0, 0, 1, -1, 1, -1, -1, 1]
    
#     def bfs(point, num):
#         q = deque()
#         visit = [[0]*3 for _ in range(4)]
#         a, b = point[0], point[1]
#         if number_pad[a][b] == num:
#             return [1, a, b]
#         q.append((a, b))
#         while q:
#             y, x = q.popleft()
#             for i in range(4):
#                 ny = y + dy[i]
#                 nx = x + dx[i]
#                 if ny < 0 or nx < 0 or ny > 3 or nx > 2 or visit[ny][nx] != 0:
#                     continue
#                 if number_pad[ny][nx] == num:
#                     return (visit[y][x] + 2, ny, nx)
#                 visit[ny][nx] = visit[y][x] + 2
#                 q.append((ny, nx))
#             for j in range(4,8):
#                 ny = y + dy[j]
#                 nx = x + dx[j]
#                 if ny < 0 or nx < 0 or ny > 3 or nx > 2 or visit[ny][nx] != 0:
#                     continue
#                 if number_pad[ny][nx] == num:
#                     return (visit[y][x] + 3, ny, nx)
#                 visit[ny][nx] = visit[y][x] + 3
#                 q.append((ny, nx))
    
#     left, right = (1, 0), (1, 2)
#     for idx in range(len(numbers)):
#         left_weight = bfs(left, numbers[idx])
#         right_weight = bfs(right, numbers[idx])
        
#         if left_weight[0] < right_weight[0]:
#             left = left_weight[1], left_weight[2]
#             answer += left_weight[0]
#         elif left_weight[0] > right_weight[0]:
#             right = right_weight[1], right_weight[2]
#             answer += right_weight[0]
#         else:
#             if idx + 1 == len(numbers):
#                 answer += left_weight[0]
#                 continue
#             next_left_weight =  bfs(left, numbers[idx+1])
#             next_right_weight =  bfs(right, numbers[idx+1])
            
#             if next_left_weight[0] >= next_right_weight[0]:
#                 left = left_weight[1], left_weight[2]
#                 answer += left_weight[0]
#             elif next_left_weight[0] < next_right_weight[0]:
#                 right = right_weight[1], right_weight[2]
#                 answer += right_weight[0]      
                
#     return answer


def solution(numbers):
    weights = ((1, 7, 6, 7, 5, 4, 5, 3, 2, 3),
               (7, 1, 2, 4, 2, 3, 5, 4, 5, 6),
               (6, 2, 1, 2, 3, 2, 3, 5, 4, 5),
               (7, 4, 2, 1, 5, 3, 2, 6, 5, 4),
               (5, 2, 3, 5, 1, 2, 4, 2, 3, 5),
               (4, 3, 2, 3, 2, 1, 2, 3, 2, 3),
               (5, 5, 3, 2, 4, 2, 1, 5, 3, 2),
               (3, 4, 5, 6, 2, 3, 5, 1, 2, 4),
               (2, 5, 4, 5, 3, 2, 3, 2, 1, 2),
               (3, 6, 5, 4, 5, 3, 2, 4, 2, 1))
    dp = {(4, 6): 0, (6, 4): 0}
    for number in numbers:
        number = int(number)
        new_dp = {}
        for (idx1, idx2), total in dp.items():
            if idx1 == number or idx2 == number:
                result = min(new_dp.get((idx1, idx2), float('inf')), total + 1)
                new_dp[(idx1, idx2)] = result
                new_dp[(idx2, idx1)] = result
            else:
                result1 = min(new_dp.get((idx1, number), float('inf')), total + weights[idx2][number])
                result2 = min(new_dp.get((idx2, number), float('inf')), total + weights[idx1][number])
                new_dp[(idx1, number)] = result1
                new_dp[(number, idx1)] = result1
                new_dp[(idx2, number)] = result2
                new_dp[(number, idx2)] = result2
        dp = new_dp
    return min(dp.values())

print(solution("1756"))
print(solution("5123"))