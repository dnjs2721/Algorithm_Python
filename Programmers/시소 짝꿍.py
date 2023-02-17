from collections import defaultdict

def solution(weights):
    answer = 0
    info = defaultdict(int)
    for w in weights:
        answer += info[w] + info[w*2] + info[w/2] + info[(w*2)/3] + info[(w*3)/2] + info[(w*4)/3] + info[(w*3)/4]
        info[w] += 1
    
    return answer

print(solution([100,180,360,100,270]))

# 2미터, 3미터, 4미터 좌석 존재
# 1:1, 2:3, 2:4(1:2), 3:4 의 비율을 가질 때 균형
# w
# w*2:w*3 = (w*2)/3, (w*3)/2
# w:w*2 = w/2, w*2
# w*3:w*4 : (w*3)/4, (w*4)/3)

# 몸무게 값 하나당 w, w*2, w/2, w*2/3, w*3/2, w*4/3, w*3/4 들이 균형비를 가지는 수 들 이다.
# 반복문을 통해 주어진 몸무게들을 차례대로 탐색하며 딕셔너리에 위 수 들을 Key로 추가하고, 자신의 Key 의 Value를 1 올려준다.
# 다음 몸무게의 균형비를 가지는 몸무게의 딕셔너리 Value 를 더해준다.