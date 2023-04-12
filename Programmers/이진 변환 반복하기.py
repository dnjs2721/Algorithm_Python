def solution(s):
    time = 0
    zero_count = 0
    while s != "1":
        time += 1
        zero_count += s.count('0')
        s = bin(len(s.replace('0', '')))[2:]

    return [time, zero_count]