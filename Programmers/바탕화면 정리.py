def solution(wallpaper):
    x = []
    y = []

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                y.append(j)
                x.append(i)

    return [min(x), min(y), max(x) + 1, max(y) + 1]


print(solution([".#...", "..#..", "...#."]))
print((solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]	)))