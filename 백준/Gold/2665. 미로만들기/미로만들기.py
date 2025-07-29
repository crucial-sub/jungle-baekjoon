from collections import deque
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    rooms = [list(input().rstrip()) for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    cost = [[-1] * n for _ in range(n)]

    q = deque()

    # 시작점 설정
    cost[0][0] = 0
    q.append((0, 0))

    while q:
        cur_x, cur_y = q.popleft()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            # 맵 경계 체크
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            
            # 아직 방문하지 않은 곳이라면 (cost가 -1이라면)
            if cost[nx][ny] == -1:
                # 하얀 방일 경우
                if rooms[nx][ny] == '1':
                    cost[nx][ny] = cost[cur_x][cur_y]
                    q.appendleft((nx, ny)) # 비용이 0인 경로는 우선적으로 탐색 (앞에 추가)
                # 검은 방일 경우
                else:
                    cost[nx][ny] = cost[cur_x][cur_y] + 1
                    q.append((nx, ny)) # 비용이 1인 경로는 나중에 탐색 (뒤에 추가)

    print(cost[n-1][n-1])

if __name__ == "__main__":
    main()