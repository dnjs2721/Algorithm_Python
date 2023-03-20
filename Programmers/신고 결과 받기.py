from collections import defaultdict

def solution(id_list, report, k):
    dic = defaultdict(set)
    dic2 = defaultdict(int)
    for id in id_list:
        dic2[id] = 0

    for i in report:
        arr = i.split()
        dic[arr[1]].add(arr[0])

    for j in dic.items():
        if len(j[1]) >= k:
            for a in j[1]:
                dic2[a] += 1

    return list(dic2.values())


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))