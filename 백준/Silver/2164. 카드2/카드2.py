from collections import deque
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    q = deque(range(1,N+1))
    while len(q)>1:
        q.popleft()     # 맨위 버리기
        if len(q) == 1:
            break
        a = q.popleft() # 두번째 카드를 빼서,
        q.append(a)     # 맨 아래로 옮기기
    print(q[0])

if __name__ == "__main__":
    main()