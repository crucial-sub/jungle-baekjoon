from collections import deque
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    rooms = [list(str(input().rstrip())) for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    cost = [[float('inf')]*(n) for _ in range(n)]

    visited = set()
    q = deque()

    visited.add((0,0,0))
    q.append((0,0,0))
    cost[0][0] = 0

    while q:
        cur_cost ,cur_x, cur_y = q.popleft()
        if cur_cost > cost[cur_x][cur_y]:
            continue
        for dir in range(4):
            nx = cur_x + dx[dir]
            ny = cur_y + dy[dir]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if (nx, ny) in visited:
                continue

            visited.add((nx, ny))
            if rooms[nx][ny] == '0':
                if cur_cost + 1 < cost[nx][ny]:
                    cost[nx][ny] = cur_cost + 1
                    q.append((cur_cost+1, nx, ny))
            elif rooms[nx][ny] == '1':
                if cur_cost < cost[nx][ny]:
                    cost[nx][ny] = cur_cost
                    q.appendleft((cur_cost, nx, ny))

    print(cost[n-1][n-1])

if __name__ == "__main__":
    main()