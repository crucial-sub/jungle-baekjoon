import sys
input = sys.stdin.readline

def main():
    N, M = map(int,input().split())
    tiny = {int(input()) for _ in range(M)}
    dp = []
    for i in range(N+1):
        j = 0
        r = []
        while (j)*(j+1)//2 < i:
            r.append(float('inf'))
            j += 1
        dp.append(r)

    dp[1][0] = 0
    dp[2][1] = 1

    for i in range(2, N+1):
        if i in tiny:
            dp[i] = [float('inf')] * len(dp[i])
            continue
        j = 1
        while (j)*(j+1)//2 < i:
            if (i-j) in tiny:
                dp[i][j] = float('inf')
            else:
                l = []
                if 0 <= j-1 < len(dp[i-j]):
                    l.append(dp[i-j][j-1] + 1)
                if 0 <= j < len(dp[i-j]):
                    l.append(dp[i-j][j] + 1)
                if 0 <= j+1 < len(dp[i-j]):
                    l.append(dp[i-j][j+1] + 1)
                if l:
                    dp[i][j] = min(l)
                else:
                    dp[i][j] = float('inf')
            j += 1
        
    print(min(dp[N]) if min(dp[N]) != float('inf') else -1)
    
if __name__ == "__main__":
    main()