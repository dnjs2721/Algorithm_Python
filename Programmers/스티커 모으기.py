# from itertools import combinations as cb

# def solution(sticker):
#     stickers = list(sticker)
#     n = len(sticker)
#     answer = 0
#     for i in list(cb(sticker, n//2)):
#         for j in range(len(i)):
            
#             standard_index = stickers.index(i[j])
                    
#             if standard_index - 1 < 0:
#                 left_index = n - 1
#             else:
#                 left_index = standard_index - 1
            
#             if standard_index + 1 > n - 1:
#                 right_index = 0
#             else:
#                 right_index = standard_index + 1
            
#             if stickers[left_index] in i or stickers[right_index] in i:
#                 break
                
#         else:
#             answer = max(answer, sum(i))
    
#     return answer
            
# print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
# print(solution([1, 3, 2, 5, 4]))

def solution(sticker):
    if len(sticker) == 1 : return sticker[0]
    
    dp1 = [0]*len(sticker) # 첫 번째 스티커를 뜯은 경우
    dp2 = [0]*len(sticker) # 첫 번째 스티컬를 뜯지 않은 경우
    
    dp1[0] = sticker[0] 
    dp1[1] = sticker[0]
    for i in range(2, len(sticker) - 1):
        dp1[i] = max(dp1[i-2] + sticker[i], dp1[i-1])
    
    dp2[1] = sticker[1]
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i-2] + sticker[i], dp2[i-1])
    
    return max(max(dp1), max(dp2))
    
print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution([1, 3, 2, 5, 4]))