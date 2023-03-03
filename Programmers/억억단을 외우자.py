def solution(e, starts):
    answer = [0 for _ in range(e+1)]
    divisor = [1 for _ in range(e+1)]
    for i in range(2, e+1):
        for j in range(i, e+1, i):
            divisor[j] += 1
            
    max_count, max_index = divisor[e], e
    answer[e] = e
    for i in range(e-1, 0, -1):
        if max_count <= divisor[i]:
            max_count = divisor[i]
            max_index = i
        answer[i] = max_index
        
    return [answer[s] for s in starts]

print(solution(8, [1,3,7]))

# 약수의 개수를 효율적으로 구하기 위해
# 1 을 e+1 개를 가진 divisor 배열 생성 (0번째 인덱스 사용 안한다.)
# 2중 for문을 이용하여 2부터 e까지의 (i)약수를 구한다. 1의 약수는 구하지 않아도 된다.
# 이때 i에서 e까지 i의 배수의 개수만큼 divisor의 i인덱스에 저장한다.

# 약수를 가장많이 가지고 있는 수의 인덱스를 저장하기 위한 배열 answer
# e 에서 1번 인덱스 방향으로 조회할 것 이기에 max_count 와 max_index 는 각각 divisor[e] 와 e로 선언
# max_count 보다 큰 값이 나오면 max_count 와 max_index 를 변경
# answer 해당 인덱스에 max_index 값을 저장

# answer[s] 를 조회하여 답 출력

# s의 목록 starts
# 각 s에 대해 서 임의의 수 n  s <= n <= e
# 즉 범위는 s 부터 e 까지

# 0 1 2 3 4 5 6 7 8
# 1 1 2 3 4 5 6 7 8
# 2 2 4 6 8 
# 3 3 6
# 4 4 8
# 5 5
# 6 6
# 7 7
# 8 8

# 1 1개 {1}
# 2 2개 {1,2}
# 3 2개 {1,3}
# 4 3개 {1,2,4}
# 5 2개 {1,5}
# 6 4개 {1,2,3,6}
# 7 2개 {1,7}
# 8 4개 {1,2,4,8}

# 각 숫자가 등장하는 횟수는 그 수의 약수의 개수와 같다.
# 모든 s에 대하여 반복하여 등장 횟수를 구하면 시간초과가 발생할 것
# 모든 범위의 끝은 항상 e이기 때문에 1부터 e 까지의 각 수의 약수를 미리 구한다.