from collections import deque

def solution(queue1, queue2):
    answer = 0
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    goal = (sum_q1 + sum_q2) / 2

    q1 = deque(queue1)
    q2 = deque(queue2)

    n = len(q1) * 4

    while sum_q1 != sum_q2 and answer <= n:
        if sum_q1 < goal:
            tmp = q2.popleft()
            sum_q1 += tmp
            sum_q2 -= tmp
            q1.append(tmp)
            answer += 1

        elif sum_q1 > goal:
            tmp = q1.popleft()
            sum_q1 -= tmp
            sum_q2 += tmp
            q2.append(tmp)
            answer += 1

    if sum_q1 != sum_q2:
        return -1

    return answer