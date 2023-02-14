#a = 97 z = 122
def solution(s, skip, index):
    skip = list(ord(i) for i in skip)
    answer = ''
    for word in s:
        cnt = index
        word = ord(word)
        while cnt != 0:
            word += 1
            if word > 122:
                word = word - 123 + 97
            if word in skip:
                continue
            cnt -= 1
        answer += chr(word)
    return answer
    
print(solution("aukks","wbqd",5))