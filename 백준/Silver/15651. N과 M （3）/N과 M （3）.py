import sys
input = sys.stdin.readline

def main():
    # 1부터 N까지 자연수 중에서 M개를 고른 수열 (중복 가능)
    N, M = map(int, input().split());
    seq = [0] * (M);

    def btk(k):
        if k == M:
            print(*seq);
            return;
        
        for i in range(1, N+1):
            seq[k] = i
            btk(k+1);

    btk(0);

if __name__ == "__main__":
    main();