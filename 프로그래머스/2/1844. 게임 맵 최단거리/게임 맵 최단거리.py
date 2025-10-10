from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    
    visited = set()
    visited.add((0, 0))
    q.append((0, 0))   
    maps[0][0] = 1
    
    while q:
        x, y = q.popleft()
        if (x, y) == (n,m):
            maps[nx][ny] += 1
            break
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if (nx, ny) in visited or maps[nx][ny] == 0:
                continue
            maps[nx][ny] += maps[x][y]
            visited.add((nx,ny))
            q.append((nx, ny))   
            
    answer = maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1
    
    return answer