import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split());
    nums = list(map(int, input().split()));
    nums.sort();
    seq = [0] * M;

    def btk(k):
        if k == M:
            print(*seq);
            return;
        
        for i in range(N):
            n = nums[i];
            seq[k] = n;
            btk(k+1);
    
    btk(0);

if __name__ == "__main__":
    main()