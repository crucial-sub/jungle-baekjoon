import sys
input = sys.stdin.readline

def multiply(mat1, mat2, n):
    """두 개의 N x N 행렬을 곱하는 함수. 각 원소는 1000으로 나눈 나머지를 저장."""
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += mat1[i][k] * mat2[k][j]
            result[i][j] %= 1000
    return result

def power(mat, b, n):
    """분할 정복을 이용해 행렬의 거듭제곱을 계산하는 함수."""
    # b가 1이면 자기 자신을 반환 (재귀의 기저 사례)
    if b == 1:
        return mat
    
    # 지수를 절반으로 나눠 재귀 호출
    # ex) A^10 = (A^5)^2
    half = power(mat, b // 2, n)
    
    # 재귀적으로 구한 half를 제곱
    result = multiply(half, half, n)
    
    # 만약 지수가 홀수였다면, A를 한 번 더 곱해준다
    # ex) A^11 = A^10 * A = (A^5)^2 * A
    if b % 2 == 1:
        result = multiply(result, mat, n)
        
    return result

def main():
    N, B = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    # B=1일 때도 각 원소를 1000으로 나눈 나머지를 처리해야 함
    if B == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] %= 1000
        result_matrix = A
    else:
        result_matrix = power(A, B, N)

    for row in result_matrix:
        print(*row)

if __name__ == "__main__":
    main()