from collections import defaultdict, deque
import sys
input = sys.stdin.readline

adj_list = defaultdict(list)

def main():
    N = int(input())
    parent = [0]*(N+1)

    for _ in range(N-1):
        node, neighbor = map(int, input().split())
        adj_list[node].append(neighbor)
        adj_list[neighbor].append(node)

    q = deque()
    q.append(1)
    visited = set()
    visited.add(1)
    while q:
        p = q.popleft()
        for child in adj_list[p]:
            if not child in visited:
                parent[child] = p
                visited.add(child)
                q.append(child)
    for i in parent[2:]:
        print(i)

if __name__ == "__main__":
    main()