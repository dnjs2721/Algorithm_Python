num = [int(input()) for _ in range(3)]
cal = list(str(num[0]*num[1]*num[2]))
arr = [0]*10
for i in cal:
    arr[int(i)] += 1
print(*arr, sep='\n')

# count 이용
# num = [int(input()) for _ in range(3)]
# cal = str(num[0]*num[1]*num[2])
# for i in range(10):
#     temp = str(i)
#     print(cal.count(temp))