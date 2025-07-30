from collections import deque
import sys
input = sys.stdin.readline

def main():
    M, N, H = map(int, input().split())
    box = {i: [list(map(int,input().split())) for _ in range(N)] for i in range(H)}
    dh = [0, 0, 0, 0, 1, -1]
    dx = [1, 0, -1, 0, 0, 0]
    dy = [0, 1, 0, -1, 0, 0]

    ripe_tomato = []
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if box[h][n][m] == 1:
                    ripe_tomato.append((h,n,m))

    q = deque(ripe_tomato)
    cnt = 0
    while q:
        q_size = len(q)
        for _ in range(q_size):
            h, x, y = q.popleft()
            
            for dir in range(6):
                nh = h + dh[dir]
                nx = x + dx[dir]
                ny = y + dy[dir]

                if not (0 <= nx < N and 0 <= ny < M and 0 <= nh < H):
                    continue
                if box[nh][nx][ny] != 0:
                    continue
                box[nh][nx][ny] = 1
                q.append((nh,nx,ny))
        if q:
            cnt += 1
    
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if box[h][n][m] == 0:
                    return print(-1)
    print(cnt)

if __name__ == "__main__":
    main()