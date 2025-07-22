from collections import deque
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    q = deque()
    for _ in range(N):
        oper = input().rstrip()
        if 'push' in oper:
            b = int(oper[5:])
            q.append(b)
        elif oper == 'pop':
            print(q.popleft() if q else -1)
        elif oper == 'size':
            print(len(q))
        elif oper == 'empty':
            print(1 if len(q) == 0 else 0)
        elif oper == 'front':
            print(q[0] if len(q) != 0 else -1)
        elif oper == 'back':
            print(q[-1] if len(q) != 0 else -1)

if __name__ == "__main__":
    main()