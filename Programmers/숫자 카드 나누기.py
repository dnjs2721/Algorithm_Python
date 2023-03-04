def solution(arrayA, arrayB):
    def two_gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    def check(arr, gcd):
        for item in arr:
            if item % gcd == 0:
                return 0
        return 1
    
    a_gcd = arrayA[0]
    b_gcd = arrayB[0]
    for i in range(len(arrayA)):
        a_gcd = two_gcd(a_gcd, arrayA[i])
        b_gcd = two_gcd(b_gcd, arrayB[i])
    
    if a_gcd == 1:
        if check(arrayA, b_gcd) == 0:
            b_gcd = 0
            
    elif b_gcd == 1:
        if check(arrayB, a_gcd) == 0:
            a_gcd = 0
    
    if a_gcd == 0 or b_gcd == 0:
        return 0
    else:           
        return max(a_gcd, b_gcd)

print(solution([10, 17], [5, 20]))
print(solution([10, 20], [5, 17]))
print(solution([14, 35, 119], [18, 30, 102]))