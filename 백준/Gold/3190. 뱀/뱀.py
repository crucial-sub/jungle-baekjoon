from collections import deque
import sys
input = sys.stdin.readline

drdc = [(0,1),(-1,0),(0,-1),(1,0)]

def get_direction(direction, rotate):
    if rotate == "L":
        return (direction+1)%4
    elif rotate == "D":
        return (direction+4-1)%4
"""
i = 0 : 오른쪽
i = 1 : 위
i = 2 : 왼쪽
i = 3 : 아래

초기 방향 : i = 0, 오른쪽
왼쪽 회전 시(L): (i+1)%4
오른쪽 회전 시(D): (i+4-1)%4
"""

def main():
    N = int(input())
    K = int(input())
    apples = [tuple(map(int,input().rstrip().split())) for _ in range(K)]
    L = int(input())
    rotates_q = deque([list(input().rstrip().split()) for _ in range(L)])

    q = deque()
    q.append((1,1))
    cur_dir = 0
    time = 0
    while True:
        time += 1
        cur_head_r, cur_head_c = q[0]
        next_head_r = cur_head_r + drdc[cur_dir][0] 
        next_head_c = cur_head_c + drdc[cur_dir][1]
        next_head = (next_head_r,next_head_c)
        if next_head_c > N or next_head_c < 1 or next_head_r > N or next_head_r < 1 or next_head in q:
            break
        q.appendleft(next_head)
        if next_head in apples:
            apples.remove(next_head)
        else:
            q.pop()

        if rotates_q and time == int(rotates_q[0][0]):
            cur_dir = get_direction(cur_dir,rotates_q[0][1])
            rotates_q.popleft()
    
    print(time)
    return

if __name__ == "__main__":
    main()