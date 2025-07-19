import sys
input = sys.stdin.readline

def main():
    M, N, L = map(int, input().split())
    data_m = list(map(int, input().split()))
    data_m.sort()
    data_n = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]
    
    hunt_cnt = 0

    for x, y in data_n:
        left = 0 # 인덱스 0
        right = M-1 # 인덱스 우측 끝
        while left <= right:
            mid = (left+right)//2

            if abs(data_m[mid]-x)+y <= L:
                hunt_cnt += 1
                break
            elif abs(data_m[mid-1]-x)+y <= L:
                hunt_cnt += 1
                break
            else:
                right = mid - 1

    print(hunt_cnt)

if __name__ == "__main__":
    main()