import sys
input = sys.stdin.readline

def main():
    T = int(input())

    for _ in range(T):
        N, M = list(map(int, input().split()))
        if N == 0:
            print(0)
            return
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if i == j:
                    dp[i][j] = 1
                if i == 1:
                    dp[i][j] = j

        for i in range(1, N + 1):
            for j in range(i - 1, M + 1):
                if i >= j:
                    continue
                for k in range(i - 1, j):
                    dp[i][j] += dp[i - 1][k]
        print(dp[N][M])


if __name__ == "__main__":
    main()
