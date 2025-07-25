from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

visited = set()
adj_list = defaultdict(list)

def main():
    V, E = map(int,input().split())
    heap = []
    total_cost = 0

    for _ in range(E):
        A, B, C = map(int, input().split())
        adj_list[A].append([C, B])
        adj_list[B].append([C, A])

    heapq.heappush(heap,[0,1])
    while len(heap) > 0:
        c, n = heapq.heappop(heap)
        if n in visited:
            continue
        else:
            visited.add(n)
            total_cost += c
        
        for neighbor in adj_list[n]:
            if not neighbor[1] in visited:
                heapq.heappush(heap, neighbor)
    print(total_cost)
    

if __name__ == "__main__":
    main()