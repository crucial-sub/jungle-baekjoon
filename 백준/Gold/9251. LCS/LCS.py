import sys
input = sys.stdin.readline

def main():
    str1 = list(input().rstrip())
    str2 = list(input().rstrip())

    n = len(str1)
    m = len(str2)

    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            char1 = str1[i-1]
            char2 = str2[j-1]
            if char1 == char2:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    
    print(dp[n][m])

if __name__ == "__main__":
    main()