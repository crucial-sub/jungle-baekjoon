from itertools import permutations
import sys
input = sys.stdin.readline

def main():
    # 1부터 N까지의 수를 M개 선택해서 나타낼 수 있는 수열을 모두 출력
    N, M = map(int, input().split());

    for p in permutations(range(1,N+1),M):
        print(*p);


if __name__ == "__main__":
    main()