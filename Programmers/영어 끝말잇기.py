def solution(n, words):
    
    # 1. 단어의 끝자리와 다음 단어의 첫 자리 확인
    ## 다르면 현재 차례와 순번 리턴
    # 2. 이미 사용된 단어 인지 확인
    ## 사용한 단어를 담을 리스트 필요
    ## 사용한 단어면 현재 차례와 순번 리턴
    # 3. 위 조건들을 통과했을 때 사용한 단어 리스트에 추가
    
    check = []
    turn = 1
    for i in enumerate(words):
        if i[0] == 0:
            check.append(i[1])
            last_ch = i[1][-1]
            turn += 1
            continue
        
        if i[1] in check:
            return [turn, i[0]//n+1]
        
        if i[1][0] == last_ch:
            check.append(i[1])
            last_ch = i[1][-1]
            turn += 1
            
        elif i[1][0] != last_ch:
            return [turn, i[0]//n+1]
              
        if turn == n+1:
            turn = 1
            
    return [0, 0]

print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))