import sys
import heapq
input = sys.stdin.readline

def main():
    N = int(input())
    
    # 왼쪽 그룹 (중간값보다 작거나 같은 값들) -> 최대 힙으로 구현
    max_heap = [] 
    
    # 오른쪽 그룹 (중간값보다 큰 값들) -> 최소 힙으로 구현
    min_heap = []

    for _ in range(N):
        num = int(input())
        
        # 1. 일단 규칙에 맞게 힙에 원소를 넣는다.
        # 최대 힙과 최소 힙의 크기가 같으면 최대 힙에, 아니면 최소 힙에 넣는다.
        # 이렇게 하면 '크기 규칙'이 거의 유지된다.
        if len(max_heap) == len(min_heap):
            # 최대 힙에는 부호를 바꿔서 넣는다.
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)
            
        # 2. '값 규칙'이 깨졌는지 확인하고 조정한다.
        # 최소 힙이 비어있지 않고, 최대 힙의 최댓값이 최소 힙의 최솟값보다 크면,
        # 두 값을 교환해준다.
        if min_heap and (-max_heap[0] > min_heap[0]):
            max_val = -heapq.heappop(max_heap)
            min_val = heapq.heappop(min_heap)
            
            heapq.heappush(max_heap, -min_val)
            heapq.heappush(min_heap, max_val)
            
        # 3. 중간값 출력
        # '크기 규칙'에 의해 중간값은 항상 최대 힙의 루트에 있다.
        print(-max_heap[0])

if __name__ == "__main__":
    main()