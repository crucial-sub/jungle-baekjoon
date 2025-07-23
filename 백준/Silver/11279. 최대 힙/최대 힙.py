import sys
import heapq
input = sys.stdin.readline

def main():
    """
    최대 힙 문제를 파이썬의 heapq(최소 힙)를 이용해 해결
    - 값 x를 힙에 넣을 때는 -x를 push
    - 힙에서 값을 꺼낼 때는 heappop()으로 나온 가장 작은 음수 값에
      다시 -를 붙여 원래의 가장 큰 양수 값으로 만듬
    """
    N = int(input())
    heap = []

    for _ in range(N):
        x = int(input())

        if x > 0:
            # 최대 힙처럼 동작하게 하기 위해, 값에 -를 붙여서 push
            heapq.heappush(heap, -x)
        else:
            # 힙이 비어있는지 확인
            if heap:
                # 가장 작은 값(가장 큰 절대값)을 pop하고, -를 붙여서 원래 값으로 변환
                print(-heapq.heappop(heap))
            else:
                # 힙이 비어있으면 0 출력
                print(0)

if __name__ == "__main__":
    main()