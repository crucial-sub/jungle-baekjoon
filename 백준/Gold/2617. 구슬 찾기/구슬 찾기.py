from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
big_adj_list = defaultdict(list)
small_adj_list = defaultdict(list)
visited = set()

def big_dfs(node):
    if node in visited:
        return
    else:
        visited.add(node)
    for neighbor in big_adj_list[node]:
        if neighbor not in visited:
            big_dfs(neighbor)

def small_dfs(node):
    if node in visited:
        return
    else:
        visited.add(node)
    for neighbor in small_adj_list[node]:
        if neighbor not in visited:
            small_dfs(neighbor)




def main():
    for _ in range(M):
        big, small = map(int, input().split())
        big_adj_list[big].append(small)
        small_adj_list[small].append(big)
    cnt = 0

    for i in range(1,N+1):
        global visited
        visited = set()
        big_dfs(i)
        if len(visited)-1 >= (N+1)//2:
            cnt += 1

    for i in range(1,N+1):
        visited = set()
        small_dfs(i)
        if len(visited)-1 >= (N+1)//2:
            cnt += 1

    print(cnt)

if __name__ == "__main__":
    main()