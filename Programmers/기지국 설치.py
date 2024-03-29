import math

def solution(n, stations, w):
    answer = 0
    dist = []
    for i in range(1, len(stations)):
        dist.append((stations[i]-w-1) - (stations[i-1]+w) )
    dist.append(stations[0]-w-1)
    dist.append(n-(stations[-1]+w))
    
    for i in dist:
        if i <= 0:
            continue
        else:
            answer += math.ceil(i / ((w*2) + 1))
    
    return answer

print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))