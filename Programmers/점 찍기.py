# 시간 초과

def solution(k, d):
    answer = 0
    
    for i in range(0, d+1):
        x = k * i
        for j in range(0, d+1):
            y = k * j
            if (x == d and y == 0) or (x == 0 and y == d):
                answer += 1
            if x < d and y < d:
                if x + y <= (d-1)*2 -1:
                    answer += 1
    
    return answer


from math import ceil

def solution2(k, d):
    answer = 0
    for x in range(0, d+1, k):
        # (0, 0) 에서 시작하기에 원의 방정식은 x^2 + y^2 = d^2
        # y^2 = d^2 - x^2
        # y = (d^2 - x^2)^0.5 -> 루트 처리
        max_y = (d ** 2 - x ** 2) ** 0.5
        # y의 최대값이 0일 때 (d, 0) 하나만 가능
        if max_y == 0:
            answer += 1
        # y의 최대값이 k로 나누어 떨어지면 1을 더해준다.
        # (x, max_y)
        else:
            answer += ceil(max_y / k)
            if max_y % k == 0:
                answer += 1
    
    return answer
        
print(solution2(2, 4))
print(solution2(1, 5))

# x, y 둘 다 d 보다 큰 수 를 가질 수 없다.
# x, y 좌표 중 하나가 d 값을 가질 경우 나머지는 무조건 0을 가진다
# x, y 둘 다 d 미만일 경우 두 값의 합은 (d-1)*2 -1 이하 
    # -> ((d-1, d-1)) 일 경우 (0, 0) 에서 와의 거리는 (d-1)*루트2 와 깉기에 d보다 큰 수 가 된다.