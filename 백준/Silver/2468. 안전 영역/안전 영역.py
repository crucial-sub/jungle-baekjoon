import sys
sys.setrecursionlimit(10000)

N = int(sys.stdin.readline())
data = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    data.append(row)

def func(h):
    is_visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if data[i][j] <= h:
                is_visited[i][j] = True

    def dfs(r, c):
        if r < 0 or r >= N or c < 0 or c >= N:
            return
        if is_visited[r][c]:
            return

        is_visited[r][c] = True
        dfs(r-1, c)
        dfs(r+1, c)
        dfs(r, c-1)
        dfs(r, c+1)

    count = 0
    for i in range(N):
        for j in range(N):
            if not is_visited[i][j]:
                dfs(i, j)
                count += 1
    return count

max_height = max(map(max, data))
max_area = 0
for h in range(0, max_height + 1):
    max_area = max(func(h), max_area)

print(max_area)
