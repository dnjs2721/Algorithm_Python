# 10분간 청소
import heapq

def solution(book_time):
    answer = 1
    time = [(int(start[:2]) * 60 + int(start[3:]), int(end[:2]) * 60 + int(end[3:])) for start, end in book_time]
    time.sort()
    
    heap = []
    for start, end in time:
        if not heap:
            heapq.heappush(heap, end + 10)
            continue
        if heap[0] <= start:
            heapq.heappop(heap)
        else:
            answer += 1
        heapq.heappush(heap, end + 10)

    return answer

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
print(solution([["09:10", "10:10"], ["10:20", "12:20"]]))
print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]))