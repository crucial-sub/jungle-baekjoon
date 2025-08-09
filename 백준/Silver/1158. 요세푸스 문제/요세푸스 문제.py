from collections import deque
import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split());

    q = deque(range(1,N+1));
    josephus = []

    while q:
        for _ in range(K-1):
            k = q.popleft();
            q.append(k)

        k = q.popleft();
        josephus.append(str(k));
    
    print(f"<{', '.join(josephus)}>")

if __name__ == "__main__":
    main()