num = input()
li = []
for i in range(0,10):
    temp = str(i)
    if i == 9:
        li[6] += num.count(temp)
    else:
        li.append(num.count(temp))
if li[6] %2 == 1:
    li[6] += 1
li[6] //= 2

print(max(li))