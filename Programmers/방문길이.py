def solution(dirs):
    answer = 0
    s = set()
    d = {"U" : [0, 1], "D" : [0, -1], "R" : [1, 0], "L" : [-1, 0]}
    
    x, y = 0, 0
    for dir in dirs:
        nx, ny = x + d[dir][0], y + d[dir][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            move1 = (x, y, nx, ny)
            move2 = (nx, ny, x, y)
            if move1 not in s:
                s.add(move1)
                s.add(move2)
                answer += 1
            x,y = nx, ny
    return answer

print(solution("LLLLRLRLRLL"))