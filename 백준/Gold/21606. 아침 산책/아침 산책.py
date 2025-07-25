from collections import defaultdict
import sys
input = sys.stdin.readline

adj_list = defaultdict(list)
visited = set()
cnt = 0

def dfs(node):
    global cnt

    for neighbor in adj_list[node]:
        if not neighbor in visited:
            if neighbor[1] == 1:
                cnt += 1
            else:
                visited.add(neighbor)
                dfs(neighbor)



def main():
    N = int(input())
    A = input()
    global cnt
    tuple_a = list(enumerate(map(int,list(A.rstrip())),start=1))

    for i in range(1, N):
        u, v = map(int, input().split())
        tuple_u, tuple_v = tuple_a[u-1], tuple_a[v-1]
        adj_list[tuple_u].append(tuple_v)
        adj_list[tuple_v].append(tuple_u)
    
    
    for a in tuple_a:
        if a[1] == 1:
            global visited
            visited = set()
            visited.add(a)
            dfs(a)
    print(cnt)

if __name__ == "__main__":
    main()