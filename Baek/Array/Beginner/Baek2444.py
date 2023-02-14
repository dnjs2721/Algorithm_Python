star = int(input())
for i in range(1, star+1):
    print(' '*(star-i) + '*'*(2*i-1))
for j in range(1, star):
    print(' '*j + '*'*(2*star-2*j-1))