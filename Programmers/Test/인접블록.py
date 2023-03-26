def solution(grid):
    answer = []
    n = len(grid)
    m = sum(list(map(int, grid[0].split())))

    arr = []
    blocks = []
    count = 0
    for i in range(n):
        temp = []
        idx = 0
        for j in list(map(int, grid[i].split())):
            for _ in range(j):
                temp.append(count)
            blocks.append([set(), [i, idx]])
            count += 1
            idx += 1
        arr.append(temp)

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(n):
        for j in range(m):
            for k in range(4):
                ny = i + dy[k]
                nx = j + dx[k]
                if ny < 0 or nx < 0 or ny >= n or nx >= m:
                    continue
                if arr[i][j] != arr[ny][nx]:
                    blocks[arr[i][j]][0].add(arr[ny][nx])

    res = sorted([[len(i[0]), i[1]] for i in blocks], reverse=True)
    answer.append(res[0][1])

    for i in range(1, len(res)):
        if res[i][0] == res[0][0]:
            answer.append(res[i][1])
        else:
            break

    return sorted(answer)


print(solution(["3 1 1 2", "2 3 2", "3 1 3"]))
print(solution(["1 1", "1 1"]))
