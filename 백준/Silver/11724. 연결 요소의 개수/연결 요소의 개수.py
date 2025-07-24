from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

adj_list = defaultdict(list)
visited = set()

def dfs(node):
    visited.add(node)

    for neighbor in adj_list[node]:
        if neighbor not in visited:
            dfs(neighbor)

def main():
    N, M = map(int,input().split())

    for _ in range(M):
        node1, node2 = list(map(int,input().split()))
        adj_list[node1].append(node2)
        adj_list[node2].append(node1)

    cnt = 0

    for i in range(1,N+1):
        if i not in visited:
            cnt += 1
            dfs(i)

    print(cnt)

if __name__ == "__main__":
    main()