import sys
input = sys.stdin.readline

def main():
    M, N, L = map(int, input().split())
    data_m = list(map(int, input().split()))
    data_m.sort()
    
    hunt_cnt = 0

    for _ in range(N): # 모든 사냥감 N개에 대해 하나씩 사대 사정거리에 포함되는지 이분탐색으로 조사
        x, y = map(int, input().split())
        if y > L: continue # y가 사정거리보다 길면 어차피 못잡음

        """
        이분탐색으로 찾고자 하는 값은 사냥감 x좌표 값에 대해 양쪽에서 가장 가까운 두 사대이다.
        여기서 가장 가까운 두 사대란 
        1. 사냥감 x좌표 왼쪽에서 가장 가까운 사대
            => 즉, 사냥감보다 x좌표 값이 작은 사대 중 마지막 사대
            => left_m: data_m[left_m] < x인 마지막 인덱스 (없으면 left_m == -1)
        2. 사냥감 x좌표보다 오른쪽에서 가장 가까운 사대 
            => 즉, 사냥감보다 x좌표 값이 크거나 같은 사대 중 첫 번째 사대
            => right_m: data_m[right_m] >= x인 첫 인덱스 (없으면 right_m == M)
        이 두 가지를 뜻한다.

        left_m = M-1, 
        right_m = 0을 초기값으로 설정해놓고
        mid 포인터를 옮겨가며 while 루프를 돌아 left_m은 x 왼쪽으로, right_m은 x 오른쪽으로 보낸다.

        즉, x선 기준으로 봤을 때
        ... left_m < 사냥감x좌표 <= right_m ... 이런식으로 된다.
        """
        left_m = M - 1
        right_m = 0
        while right_m <= left_m:
            mid = (left_m+right_m)//2
            if data_m[mid] < x:
                right_m = mid + 1 # 다음 루프 시 mid 왼쪽 탐색
            else:
                left_m = mid - 1 # 다음 루프 시 mid 오른쪽 탐색

        # 왼쪽(< x) 사대가 있으면
        if left_m >= 0 and x - data_m[left_m] + y <= L:
            hunt_cnt += 1
        # 오른쪽 사대(>= x)가 있으면
        elif right_m < M and data_m[right_m] - x + y <= L:
            hunt_cnt += 1
        

    print(hunt_cnt)

if __name__ == "__main__":
    main()