# def solution(n, l, r):
#     answer = 0
#     arr = ['11011']
#     for i in range(n-1):
#         tmp = ''
#         for j in range(len(arr[i])):
#             if arr[i][j] == '1':
#                 tmp += '11011'
#             else:
#                 tmp += '00000'
#         arr.append(tmp)
#     answer = (arr[-1][l-1:r].count('1'))
    
#     return answer

def solution(n, l, r):
    def count_bit_1(num):
        if num <= 5:
            return '11011'[:num].count('1')
        
        base = 1
        while 5 ** (base + 1) < num: # num을 넘지 않는 최대 승수를 구한다.
            base += 1
        
        section = num // (5 ** base) # num 에서 5의 base 제곱을 나눈 몫을 통해 반복되는 프랙탈의 개수를 구한다.
        remainder = num % (5 ** base) # num 에서 5의 base 제곱을 나눈 나머지를 통해 프랙탈 밖의 개수를 구한다.
        
        answer = section * (4 ** base) # 5의 base 제곱까지의 1의 개수는 4의 base 제곱이다.
        
        if section >= 3:
            answer -= (4 ** base) # 섹션이 3개 이상일 때는 0이 모여 있는 구간을 지나기에 그 구간 안에 있는 1의 개수를 빼준다.
       
        if section == 2: # 섹션이 2이면 뒤에 오는 수들은 0 이기에 추가적인 연산은 필요 없다.
            return answer
        else:
            return answer + count_bit_1(remainder) # 섹션이 3이상일 때는 
    
    return count_bit_1(r) - count_bit_1(l-1)

print(solution(2,4,17))

# 1
# 11011
# 11011 11011 00000 11011 11011