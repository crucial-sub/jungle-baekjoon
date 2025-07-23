import sys
import heapq

input = sys.stdin.readline

def main():
    n = int(input())
    people = []
    for _ in range(n):
        h, o = map(int, input().split())
        # 선분 형태로 변환
        people.append(sorted((h, o)))

    d = int(input())

    # 1. 필터링: 길이가 d보다 긴 선분은 제외
    valid_people = []
    for start, end in people:
        if end - start <= d:
            valid_people.append((start, end))

    # 2. 정렬: end 좌표 기준으로 정렬
    valid_people.sort(key=lambda x: x[1])
    
    max_count = 0
    # 3. 최소 힙: start 좌표를 저장
    start_points_heap = []

    # 4. 스위핑
    for start, end in valid_people:
        # 현재 철도의 시작 지점
        railroad_start = end - d
        
        # 현재 사람의 start를 힙에 추가
        heapq.heappush(start_points_heap, start)
        
        # 힙에서 현재 철도 범위를 벗어나는 start들을 제거
        while start_points_heap and start_points_heap[0] < railroad_start:
            heapq.heappop(start_points_heap)
            
        # 현재 힙의 크기가, 현재 철도에 포함된 사람의 수
        max_count = max(max_count, len(start_points_heap))

    print(max_count)


if __name__ == "__main__":
    main()