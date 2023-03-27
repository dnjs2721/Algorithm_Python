def solution(park, routes):
    n = len(park)
    m = len(park[0])

    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                start_y, start_x = i, j
                break

    dx = {'E': 1, 'W': -1, 'N': 0, 'S': 0}
    dy = {'E': 0, 'W': 0, 'N': -1, 'S': 1}

    for route in routes:
        way, count = route.split()
        flag = True
        for i in range(1, int(count) + 1):
            ny = start_y + dy[way] * i
            nx = start_x + dx[way] * i
            if ny < 0 or nx < 0 or ny >= n or nx >= m or park[ny][nx] == 'X':
                flag = False

        if flag:
            start_y, start_x = ny, nx

    return [start_y, start_x]


print(solution(["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"]))
print(solution(["SOO", "OXX", "OOO"], ["E 2", "S 2", "W 1"]))
print(solution(["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"]))
