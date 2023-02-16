from collections import defaultdict

def solution(weights):
    answer = 0
    info = defaultdict(int)
    for w in weights:
        print(w, w*2, w/2, w*2/3, w*3/2, w*4/3, w*3/4)
        answer += info[w] + info[w*2] + info[w/2] + info[(w*2)/3] + info[(w*3)/2] + info[(w*4)/3] + info[(w*3)/4]
        info[w] += 1
    
    return answer

print(solution([100,180,360,100,270]))
# 100 100 180 270 36