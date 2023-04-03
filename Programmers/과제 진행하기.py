def solution(plans):
    plans.sort(key=lambda x: x[1])
    answer = []
    stack = []

    for name, start, time in plans:
        start = int(start[0:2]) * 60 + int(start[3:])
        time = int(time)
        if stack:  # b_start 는 각 plan 마다 처음 extra_time 을 계산할 때 만 사용 되며
            b_name, b_start, b_time = stack.pop()
            extra_time = start - b_start

            if extra_time < b_time:  # 비교 후 stack 에 들어간 b_start 는 형식을 유지 하기 위해 삽입, 사용 되지 않는다.
                stack.append([b_name, b_start, b_time-extra_time])
            else:
                answer.append(b_name)
                extra_time = extra_time - b_time
                while stack and extra_time:
                    b_name, b_start, b_time = stack.pop()
                    if extra_time < b_time:
                        stack.append([b_name, b_start, b_time-extra_time])
                        break
                    else:
                        answer.append(b_name)
                        extra_time = extra_time - b_time

        stack.append([name, start, time])
    answer.extend([name for name, _, _ in stack[::-1]])

    return answer


print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))
print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))
