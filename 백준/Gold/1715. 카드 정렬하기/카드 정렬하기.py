import sys
import heapq
input = sys.stdin.readline

def main():
    N = int(input())
    
    heap = [int(input()) for _ in range(N)]
    heapq.heapify(heap)

    total = 0

    # 힙에 원소가 하나만 남을 때까지 반복 (하나의 묶음으로 다 합쳐질 때까지)
    while len(heap) > 1:
        # 1. 가장 작은 두 묶음을 꺼낸다
        first_smallest = heapq.heappop(heap)
        second_smallest = heapq.heappop(heap)
        
        # 2. 두 묶음을 합친다 (비교 횟수 발생)
        combined = first_smallest + second_smallest
        total += combined
        
        # 3. 합쳐진 새 묶음을 다시 힙에 넣는다
        heapq.heappush(heap, combined)

    print(total)

if __name__ == "__main__":
    main()