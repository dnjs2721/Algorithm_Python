def solution(numbers):
    arr = [i for i in range(10)]
    for num in numbers:
        arr[num] = 0
    return sum(arr)