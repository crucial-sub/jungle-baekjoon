import sys
input = sys.stdin.readline

def main():
    N = int(input());
    if (N % 5) == 0:
        print(N//5);
        return;

    dp = [-1] * (N + 3);
    dp[3] = 1;
    dp[5] = 1;
    if N <= 5: 
        print(dp[N]);
        return;

    for i in range(6, N+1):
        min_d = float("inf");
        for j in range(3, ((i+3)//2)+1):
            if (dp[j] > 0 and dp[i-j] > 0):
                min_d = min(min_d, dp[j] + dp[i-j]);
        dp[i] = min_d if min_d != float("inf") else -1;
    print(dp[N]);

if __name__ == "__main__":
    main()