import sys
input = sys.stdin.readline

def main(): 
    N, K = map(int, input().split())
    
    items = []
    for _ in range(N):
        items.append(list(map(int, input().split())))
    
    dp = [0] * (K + 1)

    for cur_w, cur_v in items:
        for w in range(K, cur_w - 1, -1):
            dp[w] = max(dp[w], cur_v + dp[w - cur_w])
    print(dp[K])

if __name__ == "__main__":
    main()