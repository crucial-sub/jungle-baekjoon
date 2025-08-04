import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        applicants = [list(map(int, input().split())) for _ in range(N)]
        applicants.sort()
        passer_min_interview = applicants[0][1]
        cnt = 1
        for i in range(1, N): 
            if applicants[i][1] < passer_min_interview:
                cnt += 1
                passer_min_interview = min(passer_min_interview, applicants[i][1])
        print(cnt)

if __name__ == "__main__":
    main()