from itertools import combinations
import sys
input = sys.stdin.readline

def main():
    # 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
    N, M = map(int, input().split());

    for c in combinations(range(1,N+1),M):
        print(*c);


if __name__ == "__main__":
    main()