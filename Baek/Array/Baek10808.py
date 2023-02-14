# 딕셔너리 이용
# import string
# dic = {}
# li = [i for i in string.ascii_lowercase]
# res = []
# str = input()
# for i in str:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1

# for j in li:
#     if j in dic:
#         res.append(dic[j])
#     else:
#         res.append(0)
# print(*res)

# ord 이용
str = input()
li = [0]*26
for i in str:
    li[ord(i)-ord('a')] += 1 
    #1. str의 i번째에 있는 알파벳을 받아 ord를 통해 해당 알파벳의 유니코드로 전환
    #2. 전환된 유니코드 X에 ord('a')를 뺀다. => X - 97 = Y
    #3. 계산하여 나온값은 li 리스트 내의 해당 알파벳 인덱스이다.
    #4. 0으로 채워진 해당 li의 해당 인덱스 값에 1을 더한다.

    #i가 b라면 ord('b') = 98
    #li[ord('b')-ord('a')] = li[98-97] = li[1]
    #li[1]은 26개의 0을 가진 li의 두번째 인덱스 이므로 b에 해당한다.
    #li[1] += 1 은 b를 탐지했다는 것을 뜻한다.
print(*li)