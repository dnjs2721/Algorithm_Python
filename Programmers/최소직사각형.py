import heapq


def solution(sizes):
    w, h = [], []
    for size in sizes:
        a, b = size
        heapq.heappush(w, -max(a, b))
        heapq.heappush(h, -min(a, b))

    return (-w[0]) * (-h[0])


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
