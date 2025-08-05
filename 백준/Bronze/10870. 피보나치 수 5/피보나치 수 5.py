import sys
input = sys.stdin.readline

def main():
    n = int(input())
    if n <= 1:
        print(n)
        return
    
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2,n+1):
        dp[i] = dp[i-1]+dp[i-2]

    print(dp[n])

if __name__ == "__main__":
    main()