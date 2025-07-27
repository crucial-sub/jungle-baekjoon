from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]

    # 1. 초기 세팅
    graph = defaultdict(list)
    in_degrees = [0] * N

    # 2. 그래프 설정 및 진입 차수 계산
    for u, v in edges:
        graph[u].append(v)
        in_degrees[v-1] += 1
    
    # 3. 진입 차수가 0인 애들 찾아서 큐에 집어넣음
    q = deque(i for i in range(1, N+1) if in_degrees[i-1] == 0)
    order = []

    # 4. 이제부터 진입차수가 0인 애들을 하나씩 찾아서 order 리스트에 담음
    while q:
        node = q.popleft()
        order.append(node) # node는 진입 차수가 0인 노드이므로 order에 append

        for neighbor in graph[node]:
            in_degrees[neighbor-1] -= 1 # node를 제거했으므로 node의 이웃들은 진입 차수 - 1

            if in_degrees[neighbor-1] == 0: # 진입차수가 0이면 큐에 담음
                q.append(neighbor)

    print(*order)


if __name__ == "__main__":
    main()