import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
max_height = max(map(max, data))

# 이동 방향: 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, h, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and data[nx][ny] > h:
                    visited[nx][ny] = True
                    q.append((nx, ny))

result = 0
for h in range(0, max_height + 1):
    visited = [[False] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and data[i][j] > h:
                bfs(i, j, h, visited)
                count += 1
    result = max(result, count)

print(result)