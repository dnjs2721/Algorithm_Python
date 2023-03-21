import string
import math

def solution(n, k):
    answer = 0
    tmp = string.digits+string.ascii_lowercase

    def convert(num, base):
        q, r = divmod(num, base)
        if q == 0:
            return tmp[r]
        else:
            return convert(q, base) + tmp[r]

    def check(x):
        if x == 1:
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

    convert_n = convert(n, k)
    arr = []
    s = ''

    for i in range(0, len(convert_n)):
        if convert_n[i] == '0':
            if len(s) == 0:
                continue
            else:
                arr.append(s)
                s = ''
        else:
            if i != 0:
                if len(s) == 0 and convert_n[i-1] != '0':
                    continue
            s += convert_n[i]

    if len(s) != 0:
        arr.append(s)

    for num in arr:
        if '0' in num:
            continue
        if check(int(num)):
            answer += 1

    return answer


print(solution(437674, 3))
print(solution(110011, 10))
