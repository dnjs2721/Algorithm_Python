def solution(n, lighthouse):
    answer = 0
    tree = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    for one, two in lighthouse:
        tree[one].append(two)
        tree[two].append(one)

    def dfs(node, tree, visited):
        visited[node] = True
        children = [nextNode for nextNode in tree[node] if not visited[nextNode]]
        on, off = 1, 0
        if not children:
            return on, off
        else:
            for child in children:
                child_on, child_off = dfs(child, tree, visited)
                on += min(child_on, child_off)
                off += child_on
            return on, off

    answer = min(dfs(1, tree, visited))
    return answer


print(solution(8, [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]))
print(solution(10, [[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]]))