def solution(lottos, win_nums):
    dic = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    count = 0
    unknown = 0
    for num in lottos:
        if num == 0:
            unknown += 1
            continue
        if num in win_nums:
            count += 1

    return [dic[count + unknown], dic[count]]
