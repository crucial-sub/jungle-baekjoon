import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    W = []
    V = []
    for _ in range(N):
        w, v = map(int, input().split())
        W.append(w)
        V.append(v)
    
    dp = [[0]*(K+1) for _ in range(N+1)]

    for i in range(1,N+1):
        cur_w = W[i-1]
        cur_v = V[i-1]
        for w in range(1,K+1):
            if cur_w > w:
                dp[i][w] = dp[i-1][w]
            else:
                dont_pack = dp[i-1][w]
                pack = cur_v + dp[i-1][w-cur_w]
                dp[i][w] = max(dont_pack, pack)
    
    print(dp[N][K])

if __name__ == "__main__":
    main()