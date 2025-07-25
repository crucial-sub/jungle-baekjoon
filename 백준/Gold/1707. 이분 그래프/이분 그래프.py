from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def bfs(v, adj_list):
    checker = [False] * (v)
    visited = set()
    q = deque()

    for i in range(1, v+1):
        if i in visited:
            continue
        visited.add(i)
        q.append(i)

        while q:
            node = q.popleft()

            for neighbor in adj_list[node]:
                if not neighbor in visited:
                    checker[neighbor-1] = not checker[node-1]
                    visited.add(neighbor)
                    q.append(neighbor)
                elif checker[neighbor-1] == checker[node-1]:
                    print('NO')
                    return
    print('YES')


def main():
    K = int(input())
    for _ in range(K):
        adj_list = defaultdict(list)

        V, E = map(int, input().split())

        for _ in range(E):
            node, neighbor = map(int, input().split())
            adj_list[node].append(neighbor)
            adj_list[neighbor].append(node)

        bfs(V, adj_list)
        

if __name__ == "__main__":
    main()