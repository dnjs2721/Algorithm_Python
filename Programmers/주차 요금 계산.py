from collections import defaultdict
import math


def solution(fees, records):
    answer = []
    dic = defaultdict(int)
    res = defaultdict(int)

    for item in records:
        time, number, op = item.split()
        if op == 'IN':
            dic[number] = (int(time[0:2]) * 60 + int(time[3:]))
        elif op == 'OUT':
            dic[number] = (int(time[0:2]) * 60 + int(time[3:])) - dic[number]
            res[number] = res[number] + dic.pop(number)

    for number, time in dic.items():
        res[number] = res[number] + (23 * 60 + 59 - time)

    res = sorted(res.items(), key=lambda x: x[0])

    for _, time in res:
        if time > fees[0]:
            answer.append(fees[1] + (math.ceil(((time-fees[0])/fees[2])) * fees[3]))
        else:
            answer.append(fees[1])

    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
