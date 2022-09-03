num = [int(input()) for _ in range(5)]
print(sum(num)//len(num))
num.sort()
print(num[2])