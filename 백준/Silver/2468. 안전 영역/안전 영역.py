from collections import deque
import sys
N = int(sys.stdin.readline())
data = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def func(h):
    is_visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if data[i][j] <= h :
                is_visited[i][j] = True
    def bfs(x, y) :
        is_visited[x][y] = True
        q = deque()
        q.append((x, y))

        while q:
            x, y = q.popleft()

            for dir in range(4): 
                nx, ny = x + dx[dir], y + dy[dir]

                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if is_visited[nx][ny] or data[nx][ny] <= h:
                    continue
                
                is_visited[nx][ny] = True
                q.append((nx, ny))
    
    count = 0
    for i in range(N):
        for j in range(N):
            if not is_visited[i][j]:
                bfs(i,j)
                count += 1
    
    return count

max_height = max(map(max, data))
max_area = 0;
for rain in range(0,max_height+1):
    max_area = max(max_area, func(rain))
print(max_area)