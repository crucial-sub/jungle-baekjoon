from collections import deque
import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    grid = [list(map(int,input().split())) for _ in range(N)]
    S, X, Y = map(int, input().split())
    if S == 0:
        print(grid[X-1][Y-1])
        return
    virus = deque()

    for k in range(1,K+1):
        for i in range(N):
            for j in range(N):
                if grid[i][j] == k:
                    virus.append((k,i,j))
                    
    visited = set()
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for _ in range(S):
        size = len(virus)
        for _ in range(size):
            k,x,y = virus.popleft()
            
            for dir in range(4):
                nx, ny = x+dx[dir], y+dy[dir]
                if nx == X-1 and ny == Y-1:
                    return print(k)
                if not (0 <= nx < N and 0 <= ny < N):
                    continue
                if (nx,ny) in visited or grid[nx][ny] != 0:
                    continue
                grid[nx][ny] = k
                virus.append((k,nx,ny))
                visited.add((k,nx,ny))
    print(0)

if __name__ == "__main__":
    main()