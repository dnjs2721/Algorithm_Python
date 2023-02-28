def solution(scores):
    answer = 1
    target = scores[0]
    target_score = sum(scores[0])
    scores.sort(key=lambda x: (-x[0], x[1])) # 1번째 점수를 기준으로 내림차순, 같은 점수일 경우 2번째 점수를 기준으로 오름차순
    
    threshold = 0
    for score in scores:
        if target[0] < score[0] and target[1] < score[1]:
            return -1
        # 앞서 1번째 점수를 기준으로 내림차순 정렬 하였기에 2번째 점수만 비교
        # 다음에 나올 점수 중 1번 점수는 앞서 나온 점수보다 같거나 작기 때문에 2번 점수만 비교
        # 2번째 점수가 크다면 앞서 나온 점수의 합보다 클 수 있기 때문에 1번째 점수랑 2번째 점수를 합하여 타겟과 비교
        # 만약 타겟의 합보다 크다면 타겟의 등수 보다 높은 점수 이기에 타겟의 등수를 +1 해 준다.
        # 그 후 threshold 에 지금의 2번째 점수를 등록
        if threshold <= score[1]:
            if target_score < score[0] + score[1]:
                answer += 1
            threshold = score[1]
            
    return answer

print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]]))