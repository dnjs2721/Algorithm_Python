num = []
odd_num = []
for i in range(7):
    num.append(int(input()))

for i in num:
    if i%2 == 1:
        odd_num.append(i)

print(f'{sum(odd_num)}\n{min(odd_num)}' if len(odd_num) != 0 else "-1")