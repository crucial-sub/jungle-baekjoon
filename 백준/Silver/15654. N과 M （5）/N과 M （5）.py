import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split());
    nums = list(map(int, input().split()));
    nums.sort();
    seq = [0] * M;
    is_used = set();

    def btk(k):
        if k == M:
            print(*seq);
            return;
        
        for i in range(N):
            n = nums[i];
            if n not in is_used:
                seq[k] = n;
                is_used.add(n);
                btk(k+1);
                is_used.remove(n);
    
    btk(0);

if __name__ == "__main__":
    main()