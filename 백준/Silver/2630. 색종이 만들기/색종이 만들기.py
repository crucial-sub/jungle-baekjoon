import sys
input = sys.stdin.readline

cnt = [0, 0]

def div_arr(arr,rs,re,cs,ce):
    divided = []
    for r in arr[rs:re]:
        r_arr = []
        for c in r[cs:ce]:
            r_arr.append(c)
        divided.append(r_arr)
    return divided

def recur(arr, n):
    if n <= 1: 
        cnt[arr[0][0]] += 1
        return
    
    ## 중복 검사
    base = arr[0][0]
    same = True
    for i in range(n):
        for j in range(n):
            if arr[i][j] != base:
                same = False
                break
        if not same:
            break
    if same:
        cnt[base] += 1
        return

    ## 미통과시 분할 재귀
    recur(div_arr(arr,0,n//2,0,n//2),n//2)
    recur(div_arr(arr,0,n//2,n//2,n),n//2)
    recur(div_arr(arr,n//2,n,0,n//2),n//2)
    recur(div_arr(arr,n//2,n,n//2,n),n//2)

def main():
    N = int(input())
    cp = [list(map(int,input().rstrip().split())) for _ in range(N)]
    recur(cp, N)

    for i in cnt:
        print(i)

if __name__ == "__main__":
    
    main()