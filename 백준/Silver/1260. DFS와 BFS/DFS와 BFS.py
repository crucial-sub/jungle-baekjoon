import sys
input = sys.stdin.readline

from collections import defaultdict, deque

adj_list = defaultdict(list)

def dfs(start_node):
    visited = set()
    order = []

    def recur(node):
        if node not in visited:
            visited.add(node)
            order.append(node)
        else:
            return    
        for neighbor in adj_list[node]:
            recur(neighbor)

    recur(start_node)
    return order


def bfs(start_node):
    visited = set()
    order = []
    q = deque([start_node])
    visited.add(start_node)

    while q:
        node = q.popleft()
        order.append(node)

        for neighbor in adj_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
    return order

def main():
    N, M, V = map(int, input().split())
    
    for _ in range(M):
        node1, node2 = list(map(int,input().split()))
        adj_list[node1].append(node2)
        adj_list[node2].append(node1)

    for key in adj_list:
        adj_list[key].sort()
    
    dfs_path = dfs(V)
    print(*dfs_path)
    bfs_path = bfs(V)
    print(*bfs_path)


if __name__ == "__main__":
    main()