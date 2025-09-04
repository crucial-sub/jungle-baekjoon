import sys
input = sys.stdin.readline


def main():
    N = int(input())
    if N == 1:
        print(0)
        return
    if N <= 3:
        print(1)
        return
    dp = [0] * (N + 1)
    dp[2] = 1
    dp[3] = 1

    for i in range(4, N + 1):
        min_i = dp[i - 1]
        if (i % 2) == 0:
            min_i = min(min_i, dp[i // 2])
        if (i % 3) == 0:
            min_i = min(min_i, dp[i // 3])
        dp[i] = min_i + 1
    print(dp[N])


if __name__ == "__main__":
    main()
