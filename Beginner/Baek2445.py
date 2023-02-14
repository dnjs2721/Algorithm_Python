star = int(input())
for i in range(1,star+1):
    print('*'*i + ' '*(2*star-2*i) + '*'*i)
for j in range(1,star):
    print('*'*(star-j) + ' '*(2*j) + '*'*(star-j))