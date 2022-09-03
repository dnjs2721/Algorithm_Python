# arr = [list(map(int, input().split())) for _ in range(10)]
# origin=[]
# cha=[]
# temp=[]
# for i in range(1,21):
#     origin.append(i)

# for j in range(10):
#     temp= arr[j]
#     a,b = temp[0], temp[1]
#     cha.append(origin[a-1:b])
#     cha = sum(cha, [])
#     cha = cha[::-1]
#     origin[a-1:b] = cha
#     cha.clear()
# print(*origin) 


origin = [i for i in range(1,21)]
for _ in range(10):
    x, y = map(int,input().split())
    temp = origin[x-1:y]
    temp = temp[::-1]
    origin[x-1:y] = temp
print(*origin)
