from collections import defaultdict
import sys
input = sys.stdin.readline

visited = set()
adj_list = defaultdict(list)
cnt = 0

def dfs(node):
    global cnt
    if node in visited:
        return
    else:
        cnt += 1
        visited.add(node)

    for neighbor in adj_list[node]:
        if not neighbor in visited:
            dfs(neighbor)

def main():
    V = int(input())
    E = int(input())
    

    for _ in range(E):
        node, neighbor = map(int, input().split())
        adj_list[node].append(neighbor)
        adj_list[neighbor].append(node)
    
    dfs(1)

    print(cnt-1)


if __name__ == "__main__":
    main()