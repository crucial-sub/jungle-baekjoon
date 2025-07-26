from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def main():
    N, M, K, X = map(int, input().split())
    adj_list = defaultdict(list)
    for _ in range(M):
        A, B = map(int, input().split())
        adj_list[A].append(B)
    visited = set()

    q = deque()
    visited.add(X)
    q.append((X,0))
    ans = []
    while q:
        c, d = q.popleft()
        if d == K:
            ans.append(c)
        for neighbor in adj_list[c]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append((neighbor,d+1))

    if len(ans) == 0:
        print(-1)
    else:
        ans.sort()
        for city in ans:
            print(city)

if __name__ == "__main__":
    main()