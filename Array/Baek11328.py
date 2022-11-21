for _ in range(int(input())):
    A, B = input().split()
    A = sorted(A); B= sorted(B)
    if A == B:
        print('Possible')
    else:
        print('Impossible')   

# N =  int(input())

# for _ in range(N):
#     A, B = input().split()
#     A =  (''.join(sorted(A)))
#     B =  (''.join(sorted(B)))

#     if len(A) != len(B):
#         print('Impossible')
#         continue
    
#     for i in range(len(A)):
#         if A[i] == B[i]:
#             flag = True
#         else:
#             flag = False
#             break
    
#     if flag:
#         print('Possible')
#     else:
#         print('Impossible')