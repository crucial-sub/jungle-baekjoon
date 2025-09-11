import sys
input = sys.stdin.readline


def main():
    N = int(input())
    tips = [int(input()) for _ in range(N)]
    tips.sort(reverse=True)
    res = 0
    for i in range(N):
        if tips[i] - i <= 0:
            break
        res += tips[i] - i

    print(res)

if __name__ == "__main__":
    main()
