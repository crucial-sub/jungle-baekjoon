import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    A = [int(input().rstrip()) for _ in range(N)]

    cnt = 0
    remains = K
    for i in range(N-1,-1,-1):
        coin = A[i]
        if remains < A[0]:
            break
        if coin > remains:
            continue
        cnt += remains // coin
        remains = remains % coin
    print(cnt)
    
if __name__ == "__main__":
    main()