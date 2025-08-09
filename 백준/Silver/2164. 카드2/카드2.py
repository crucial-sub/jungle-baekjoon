from collections import deque
import sys
input = sys.stdin.readline

def main():
    N = int(input());
    if(N == 1):
        print(1);
        return;

    q = deque(range(1,N+1));

    while q:
        q.popleft();
        if len(q) <= 1:
            break;
        a = q.popleft();
        q.append(a);
    print(q[0]);
    
if __name__ == "__main__":
    main()