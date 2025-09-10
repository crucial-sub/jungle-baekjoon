import sys
input = sys.stdin.readline

def main():
    N = int(input())
    w = [int(input()) for _ in range(N)]
    w.sort()
    max_w = w[-1]

    for i in range(N):
        max_w = max(max_w, (N - i) * w[i])

    print(max_w)

if __name__ == "__main__":
    main()
