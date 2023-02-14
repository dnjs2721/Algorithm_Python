Number = sorted(map(int, input().split()), reverse=True)

if Number[0] == Number[1] == Number[2]:
    print(10000+Number[0]*1000)
elif Number[0] == Number[1] or Number[0] == Number[2]:
    print(1000+Number[0]*100)
elif Number[1] == Number[2]:
    print(1000+Number[1]*100)
else:
    print(100*Number[0])