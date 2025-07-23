import sys

# 재귀 깊이 제한 설정 (N이 크므로 필수)
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def get_dist_sq(p1, p2):
    """두 점 사이의 거리의 제곱을 반환하는 함수."""
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def solve(points, n):
    # 점이 1개면 무한대 거리 반환
    if n == 1:
        return float('inf')
    # 점이 2개나 3개면 그냥 직접 계산 (브루트포스)
    if n <= 3:
        min_dist = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                min_dist = min(min_dist, get_dist_sq(points[i], points[j]))
        return min_dist

    # 1. 분할 (Divide)
    mid_idx = n // 2
    mid_x = points[mid_idx][0]

    # 2. 정복 (Conquer)
    d_left = solve(points[:mid_idx], mid_idx)
    d_right = solve(points[mid_idx:], n - mid_idx)
    
    min_dist = min(d_left, d_right)

    # 3. 결합 (Combine) - 스트립 내부의 점들 확인
    strip_points = []
    for i in range(n):
        if (points[i][0] - mid_x)**2 < min_dist:
            strip_points.append(points[i])
            
    # 스트립 내부의 점들을 y좌표 기준으로 정렬
    strip_points.sort(key=lambda p: p[1])
    
    # 스트립 내부에서 더 가까운 점 쌍 찾기
    for i in range(len(strip_points)):
        for j in range(i + 1, len(strip_points)):
            # y좌표 차이가 현재 최소 거리(d)보다 크면 더 이상 볼 필요 없음
            if (strip_points[j][1] - strip_points[i][1])**2 >= min_dist:
                break
            dist = get_dist_sq(strip_points[i], strip_points[j])
            min_dist = min(min_dist, dist)
            
    return min_dist


def main():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]

    # 0. 사전 준비: x좌표 기준 정렬
    points.sort()
    
    print(solve(points, n))


if __name__ == "__main__":
    main()