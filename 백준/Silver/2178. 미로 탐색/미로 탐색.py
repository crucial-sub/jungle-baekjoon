from collections import deque
import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    maze = [list(map(int,list(input().rstrip()))) for _ in range(N)]
    visited = set()
    # 하우상좌
    dx = [1, 0, -1, 0]  # 행 변화량
    dy = [0, 1, 0, -1]  # 열 변화량
    q = deque()
    visited.add((0,0))
    q.append((0, 0, 1))
    while q:
        x, y, d = q.popleft()
        if (x,y) == (N-1,M-1):
            print(d)
            return 
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if (nx, ny) in visited or maze[nx][ny] == 0:
                continue
            visited.add((nx,ny))
            q.append((nx, ny, d+1))

if __name__ == "__main__":
    main()