from collections import deque
import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    q = deque(range(1,N+1))
    arr = []
    while q:
        for _ in range(K-1):
            head = q.popleft()
            if not q:
                arr.append(head)
                print("<" + ", ".join(map(str, arr)) + ">")
                return                
            q.append(head)
        arr.append(q.popleft())

    print("<" + ", ".join(map(str, arr)) + ">")
if __name__ == "__main__":
    main()