import sys
N = int(sys.stdin.readline())

# 이전 퀸들이 각 공격 루트의 어느 부분을 차지 중인지 체크
col_check = [False]*N # column 방향 공격 루트 체크
diagonal_check1 = [False]*(2*N-1) # / 방향 대각선 루트 체크
diagonal_check2 = [False]*(2*N-1) # \ 방향 대각선 루트 체크

count = 0

def func(r):  # r = 현재 퀸을 놓을 행
    global count
    if r == N: # N-1행에 퀸이 놓여져 있으면 count 증가시키고 그대로 return
        count += 1
        return

    for i in range(N):  # r행 i열에 퀸을 놓을지 판단
        # 1. col_check[i]: 이전 퀸들이 i열을 공격 루트로 삼고있는지 체크
        # 2. diagonal_check1[(0 + i) + (0 + r)]: (0,0)기준으로 i열, r행만큼 떨어진 곳에 있는 "/" 방향 대각선을 이전 퀸들이 공격 루트로 삼고 있는지 체크
        # 3. diagonal_check2[((N-1) - i) + (0 + r)]: (N-1,0)기준으로 i열, r행만큼 떨어진 곳에 있는 "\" 방향 대각선을 이전 퀸들이 공격 루트로 삼고 있는지 체크
        if col_check[i] or diagonal_check1[i + r] or diagonal_check2[N - 1 - i + r]: 
            continue # 공격 루트에 하나라도 걸리면 다음 i열로 루프 이동
        # r행 i열에 퀸을 놓고(해당 퀸의 공격 루트들 모두 True로 바꿈) 다음 행으로 이동
        col_check[i] = True 
        diagonal_check1[i + r] = True
        diagonal_check2[N - 1 - i + r] = True
        func(r + 1)
        # 백 트래킹을 위해 r행 i열에 퀸을 놓았던 것을 취소
        col_check[i] = False
        diagonal_check1[i + r] = False
        diagonal_check2[r - i + N - 1] = False

func(0)
print(count)