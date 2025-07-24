import sys
input = sys.stdin.readline

from collections import defaultdict, deque

class GraphList:
    def __init__(self):
        self.adj_list = defaultdict(list)


    def add_edge(self, u, v):
        # 무방향 그래프이므로 양쪽 모두의 리스트에 추가
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def __str__(self):
        return "\n".join([f"{vertex}: {neighbors}" for vertex, neighbors in self.adj_list.items()])

    def dfs(self, start_node):
        visited = set() # 방문한 노드를 기록하기 위한 집합
        order = []      # 탐색 순서를 기록하기 위한 리스트

        # 실제 재귀 탐색을 수행할 내부 함수
        def _dfs_recursive(node):
            # 현재 노드를 방문 처리
            if node in visited:
                return
            visited.add(node)
            order.append(node)

            # 현재 노드와 인접한 모든 노드에 대해 재귀적으로 방문
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    _dfs_recursive(neighbor)
            
        _dfs_recursive(start_node)
        return order

    def bfs(self, start_node):
        visited = set() # 방문한 노드를 기록하기 위한 집합
        order = []      # 탐색 순서를 기록하기 위한 리스트

        q = deque([start_node]) # 탐색할 노드를 담아둘 큐

        visited.add(start_node) # 시작 노드를 방문 처리

        while q:
            # 큐의 맨 앞에서 노드를 하나 꺼냄
            node = q.popleft()
            order.append(node)

            # 현재 노드와 인접한 모든 노드를 확인
            for neighbor in self.adj_list[node]:
                # 아직 방문하지 않은 노드라면
                if neighbor not in visited:
                    # 방문 처리하고 큐에 추가
                    visited.add(neighbor)
                    q.append(neighbor)
        
        return order



def main():
    N, M, V = map(int, input().split())
    g = GraphList()
    for _ in range(M):
        node1, node2 = map(int, input().split())
        g.add_edge(node1,node2)

    for key in g.adj_list:
        g.adj_list[key].sort()

   # 시작 정점이 그래프에 존재하는 경우에만 탐색 수행
    if V in g.adj_list:
        dfs_path = g.dfs(V)
        print(*dfs_path)

        bfs_path = g.bfs(V)
        print(*bfs_path)
    else:
        print(V)
        print(V)



if __name__ == "__main__":
    main()