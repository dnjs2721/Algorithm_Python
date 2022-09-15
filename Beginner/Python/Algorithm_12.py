from itertools import combinations

num=[int(input()) for _ in range(9)]

for i in combinations(num, 7):
    if sum(i)==100:
        for j in sorted(i):
            print(j)
        break

# num=[int(input()) for _ in range(9)]

# for i in range(9):
#     for j in range(i+1, 9):
#         if sum(num) - (num[i]+num[j]) == 100:
#             target1, target2 = num[i], num[j]
#             break

# num.remove(target1)
# num.remove(target2)

# for k in sorted(num):
#     print(k)