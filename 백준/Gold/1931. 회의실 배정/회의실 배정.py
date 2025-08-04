import sys
input = sys.stdin.readline

def main():
    N = int(input())
    meetings = [list(map(int, input().split())) for _ in range(N)]
    meetings.sort(key=lambda x: (x[1], x[0]))
    
    cnt = 1
    prev_end = meetings[0][1]
    for i in range(1,N):
        start, end = meetings[i]
        if start < prev_end:
            continue
        prev_end = end
        cnt += 1
    print(cnt)



if __name__ == "__main__":
    main()