def solution(storey):
    answer = 0
    while storey != 0:
        n = storey % 10
        
        if n >= 6 : # 나머지가 6보다 크다면 자릿수를 올려준다
            storey += 10 - n # 10 에서 나머지를 뺀 만큼이 움직이는 층 수
            answer += 10 - n
            
        elif n == 5 and (storey // 10) % 10 >= 5 : # 나머지가 5이고 앞자리가 5와 같거나 클 때
            storey += 10 - n
            answer += 10 - n
        
        else: # 나머지가 5보다 작거나, 나머지가 5이나 앞자리가 5보다 작을 때 answer 값만 올려준다
            answer += n
        
        # 나머지가 5보다 작은 상태에서 이 단계에 오면 storey // 10 연산으로 나머지는 버려지기에 따로 연산이 필요없다.
        # 10을 나눈 몫으로 storey를 저장하기에 자릿수 하나를 올리는 연산이랑 같다.
        storey = storey // 10
            
    return answer

print(solution(2554))