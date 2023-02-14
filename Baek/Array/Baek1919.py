lst = [0]*26

for i in input():
    lst[ord(i)-97] += 1
for j in input():
    lst[ord(j)-97] -= 1

print(sum(map(abs, lst)))