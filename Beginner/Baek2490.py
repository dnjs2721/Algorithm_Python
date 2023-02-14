first = list(map(int, input().split()))
second = list(map(int, input().split()))
third = list(map(int, input().split()))

def case(a):
    print("ABCD"[a.count(0)-1] if a.count(0)!=0 else "E")              

case(first)
case(second)
case(third)