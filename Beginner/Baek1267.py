count = int(input())
time = list(map(int,input().split()))

Yprice = []
Mprice = []

for i in time:
    Ytemp = (i // 30 + 1) * 10
    Yprice.append(Ytemp)
    Mtemp = (i // 60 + 1) * 15
    Mprice.append(Mtemp)

if sum(Yprice) < sum(Mprice):
    print(f'Y {sum(Yprice)}')
elif sum(Yprice) > sum(Mprice):
    print(f'M {sum(Mprice)}')
else:
    print(f'Y M {sum(Yprice)}')