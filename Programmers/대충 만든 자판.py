from collections import defaultdict

def solution(keymap, targets):
    answer = []
    keydict = defaultdict(int)
    for i in keymap:
        for j in range(len(i)):
            if keydict[i[j]] == 0:
                keydict[i[j]] = j+1
            if keydict[i[j]] > j + 1:
                keydict[i[j]] = j+1
        
    for i in targets:
        res = 0
        for j in i:
            if keydict[j] == 0:
                answer.append(-1)
                break
            res += keydict[j]
        else:
            answer.append(res)

    return answer

print(solution(["ABACD", "BCEFD"], ["ABCD","H"]))