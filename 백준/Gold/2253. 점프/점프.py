import sys
input = sys.stdin.readline

def main():
    N, M = map(int,input().split())
    tiny_stones = {int(input()) for _ in range(M)}
    dp = []
    for i in range(N+1):
        j = 0
        r = []
        while (j)*(j+1)//2 < i:
            r.append(float('inf'))
            j += 1
        dp.append(r)

    dp[1][0] = 0

    for i in range(2, N+1):
        if i in tiny_stones:
            continue
        
        for j in range(1, len(dp[i])):
            jumps = []
            if j-1 < len(dp[i-j]):
                jumps.append(dp[i-j][j-1] + 1)
            if j < len(dp[i-j]):
                jumps.append(dp[i-j][j] + 1)
            if j+1 < len(dp[i-j]):
                jumps.append(dp[i-j][j+1] + 1)
                
            if jumps:
                dp[i][j] = min(jumps)
            else:
                dp[i][j] = float('inf')
        
    print(min(dp[N]) if min(dp[N]) != float('inf') else -1)
    
if __name__ == "__main__":
    main()