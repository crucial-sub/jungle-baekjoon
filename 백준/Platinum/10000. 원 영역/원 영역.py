import sys
sys.setrecursionlimit(10**6) # 재귀 깊이 제한 해제
input = sys.stdin.readline

class CircleNode:
    """각 원을 표현하는 클래스"""
    def __init__(self, id, left, right):
        self.id = id
        self.left = left
        self.right = right
        self.diameter = right - left
        self.children = []

def dfs_calculate_areas(node, total_areas):
    """DFS로 트리를 순회하며 추가 영역을 계산"""
    
    # 1. 자식들의 지름의 합을 계산
    children_diameter_sum = 0
    for child in node.children:
        # 자식 노드에 대해 재귀적으로 먼저 계산하고,
        # 반환된 total_areas를 업데이트
        total_areas = dfs_calculate_areas(child, total_areas)
        children_diameter_sum += child.diameter
    
    # 2. 추가 영역 발생 조건 확인
    # (루트 노드는 가짜 노드이므로 제외)
    if node.id != -1 and node.diameter == children_diameter_sum:
        total_areas += 1
        
    return total_areas

def main():
    N = int(input())
    circles = []
    for i in range(N):
        x, r = map(int, input().split())
        circles.append(CircleNode(i, x - r, x + r))

    # 1. 정렬: left 오름차순, right 내림차순
    circles.sort(key=lambda c: (c.left, -c.right))
    
    # 2. 트리 구축
    # 최상위 가상 노드 (모든 원을 포함)
    root = CircleNode(-1, -float('inf'), float('inf')) 
    parent_candidates = [root] # 부모 후보 스택

    for circle in circles:
        # 현재 원을 포함할 수 없는 부모 후보들을 스택에서 제거
        while parent_candidates[-1].right < circle.right:
            parent_candidates.pop()
        
        # 스택의 top이 현재 원의 직계 부모
        parent = parent_candidates[-1]
        parent.children.append(circle)
        
        # 현재 원도 다른 원의 부모가 될 수 있으므로 스택에 추가
        parent_candidates.append(circle)
    
    # 3. 영역 계산
    # 기본 영역(N+1) + 재귀 호출로 찾은 추가 영역
    initial_areas = N + 1
    total_areas = dfs_calculate_areas(root, initial_areas)
    
    print(total_areas)

if __name__ == "__main__":
    main()