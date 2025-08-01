import sys
input = input

T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input()) 
    
    dp = [[0] * (M+1) for _ in range(N+1)]
    
    for i in range(N+1):
        dp[i][0] = 1
        
    for i in range(1,N+1):
        coin_value = coins[i-1]
        for j in range(1,M+1):
            dont_use = dp[i-1][j]
            
            use = 0
            if coin_value <= j:
                use = dp[i][j - coin_value]
            
            dp[i][j] = dont_use + use
            
    print(dp[N][M])
    