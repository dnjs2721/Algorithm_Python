# N, K = map(int,input().split())
# SY = [list(map(int,input().split()))for _ in range(N)]
# grade = [[0,0] for _ in range(6)]
# room=0

# for i in range(N):
#     temp = SY[i]
#     for j in range(6):
#         if temp[0] == 1:
#             if temp[1] == j+1:
#                 grade[j][0] += 1
#         else:
#             if temp[1] == j+1:
#                 grade[j][1] += 1

# for l in range(6):
#     temp2 = grade[l]
#     for n in temp2:
#         if n > 0 and n % K > 0 :
#             room += n // K + 1
#         else:
#             room += n // K

# print(room)

N, K = map(int, input().split())
res = [[0]*6, [0]*6]
rooms = 0

for i in range(N):
    A, B = map(int, input().split())
    res[A][B-1] += 1

for j in range(2):
    for n in range(6):
        tmp = res[j][n]
        if tmp % K > 0:
            rooms += tmp//K + 1
        else:
            rooms += tmp//K

print(rooms)