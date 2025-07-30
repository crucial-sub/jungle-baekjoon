from collections import deque
import sys
input = sys.stdin.readline

def main():
    R, C = map(int, input().split())
    forest = [list(input().rstrip()) for _ in range(R)]
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]
    water = []
    for r in range(R):
        for c in range(C):
            point = forest[r][c]
            if point == 'D':
                d = (r,c)
            elif point == 'S':
                s = (r,c)
            elif point == '*':
                water.append((r,c))

    water_q = deque(water)
    s_q = deque()
    s_q.append(s)

    time = 0

    w_visited = set()
    s_visited = set()

    while s_q:
        size_wq = len(water_q)
        size_sq = len(s_q)

        for _ in range(size_wq):
            wr, wc = water_q.popleft()
            for dir in range(4):
                nr = wr + dr[dir]
                nc = wc + dc[dir]

                if not (0 <= nr < R and 0 <= nc < C):
                    continue
                if forest[nr][nc] == 'X' or forest[nr][nc] == 'D' or (nr,nc) in w_visited:
                    continue
                forest[nr][nc] = '*'
                water_q.append((nr,nc))
                w_visited.add((nr,nc))

        for _ in range(size_sq):
            sr, sc = s_q.popleft()
            for dir in range(4):
                nr = sr + dr[dir]
                nc = sc + dc[dir]

                if not (0 <= nr < R and 0 <= nc < C):
                    continue
                if forest[nr][nc] == '*' or forest[nr][nc] == 'X' or (nr,nc) in s_visited:
                    continue
                if forest[nr][nc] == 'D':
                    print(time+1)
                    return
                forest[nr][nc] = 'S'
                s_q.append((nr,nc))
                s_visited.add((nr,nc))

        time += 1
    print('KAKTUS')


if __name__ == "__main__":
    main()