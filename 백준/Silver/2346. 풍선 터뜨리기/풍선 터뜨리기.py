from collections import deque
import sys
input = sys.stdin.readline

def main():
    N = int(input());
    D = list(map(int, input().split()));
    deq = deque(range(1,N+1));
    ans = [];
    while deq:
        balloon = deq.popleft();
        d = D[balloon-1];
        if d > 0: deq.rotate(-(d-1));
        else: deq.rotate(-d);
        ans.append(balloon);

    print(*ans);

if __name__ == "__main__":
    main()