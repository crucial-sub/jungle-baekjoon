from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    M = int(input())

    needs = [[0]*(N+1) for _ in range(N+1)]
    adj_list = defaultdict(list)
    in_degree = [0] * (N)

    for _ in range(M):
        X, Y, K = map(int, input().split())
        adj_list[Y].append((X,K))
        in_degree[X-1] += 1
    
    q = deque(i for i in range(1, N+1) if in_degree[i-1] == 0)
    for i in q:
        needs[i][i] = 1
    
    basic = [*q]

    while q:
        part = q.popleft()

        for upper_part, k in adj_list[part]:
            for j in basic:
                needs[upper_part][j] += needs[part][j] * k
            
            in_degree[upper_part-1] -= 1

            if in_degree[upper_part-1] == 0:
                q.append(upper_part)
    
    for i in basic:
        print(i, needs[N][i])

if __name__ == "__main__":
    main()