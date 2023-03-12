def solution(order):
    assist = []
    i = 1
    cnt = 0 
    while i != len(order)+1:
        assist.append(i)
        while assist and assist[-1] == order[cnt]:
            cnt += 1
            assist.pop()  
        i += 1
    return cnt

print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))

# 택배 상자는 모두 크기가 같다
# 1번 부터 n번 까지 순서대로 영재에게 전달된다
# 택배상자는 1번부터 내릴 수 있다
# 택배를 실을 때는 주어진 순서대로 실어야 한다.
# 순서가 아닌 택배는 보조 벨트에 올린다.
# 보조 벨트에 올린 택배는 선입후출이다
# 보조 벨트를 이용하여도 원하는 순서대로 싣지 못 한다면 그만

# n이 5일 때 
# 영재 보유 택배 순서 1, 2, 3, 4, 5 
# 싣는 순서 4, 3, 1, 2, 5
# 보조에 1, 2, 3 을 뺀 후 4 를 싣는다
# 보조에서 3을 싣는다
# 1 상자는 보조에 있지만 2 뒤에 나오기 때문에 더 이상 상자를 싣지 않고 그만
# 2개 return