import sys
input = sys.stdin.readline

def multiply_matrix(mat1, mat2):
    return mat1[0] * mat1[1] * mat2[1]

def main():
    N = int(input())
    matrix_list = [list(map(int,input().split())) for _ in range(N)]

    # dp[i][j]: i번째 행렬부터 j번째 행렬까지 곱할 때 최소 곱셈 연산 횟수
    dp = [[0] * (N+1) for _ in range(N+1)]

    # 최종 목표는 길이가 N인 구간에서 최소 곱셈 연산 횟수, 즉 dp[1][N]을 구하는 것.
    # 이를 위해 길이가 짧은 구간부터 긴 구간 순서로 DP 테이블을 채워나간다.

    # L: 합칠 행렬의 개수(구간의 길이). 2개부터 N개까지 점차 늘려나간다.
    for L in range(2, N+1):
        
        # i: 구간의 시작 행렬 번호
        # 길이가 L인 구간의 마지막 시작점은 N-L+1 이므로, range의 끝은 N-L+2가 된다.
        for i in range(1, N-L+2):

            # j: 구간의 마지막 행렬 번호
            j = i + L - 1

            l = []
            for k in range(i,j):
                l.append(dp[i][k] + dp[k+1][j] + multiply_matrix([matrix_list[i-1][0], matrix_list[k-1][1]],[matrix_list[k][0],matrix_list[j-1][1]]))
            dp[i][j] = min(l) if l else 0                

    print(dp[1][N])

if __name__ == "__main__":
    main()