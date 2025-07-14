import sys
N, M = map(int, sys.stdin.readline().split())
arr = [0] * M           # 현재 선택된 숫자를 저장할 리스트
isused = [False] * (N+1)  # 1부터 n까지 사용 여부 표시

def func(k):
    if k == M:  # m개를 모두 선택한 경우
        print(*arr)
        return

    for i in range(1, N+1):  # 1부터 n까지 숫자 중에서
        if not isused[i]:    # 아직 사용하지 않은 수면
            arr[k] = i
            isused[i] = True
            func(k + 1)      # 다음 자리 수 정하러 재귀 호출
            isused[i] = False  # 백트래킹 (원상 복구)
func(0)