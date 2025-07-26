import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    M = int(input())
    bus_graph = defaultdict(dict)
    for _ in range(M):
        bus, city, cost = map(int, input().split())
        if city in bus_graph[bus]:
            cost = min(cost, bus_graph[bus][city])
        bus_graph[bus][city] = cost
    start_city, target_city = map(int, input().split())
    distances = defaultdict(int)
    for city in range(1,N+1):
        distances[city] = float('inf')
    distances[start_city] = 0
    pq = [(0,start_city)]

    while pq:
        cur_dist, cur_node = heapq.heappop(pq)

        if cur_dist > distances[cur_node]:
            continue
        
        for neighbor, cost in bus_graph[cur_node].items():
            distance = cur_dist + cost
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq,(distance, neighbor))
    
    print(distances[target_city])

if __name__ == "__main__":
    main()