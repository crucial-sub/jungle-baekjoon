import sys
N, r, c = map(int, sys.stdin.readline().split())

def func(n, r, c):
    if n == 0:
        return 0
    half = 2 ** (n - 1)
    
    # 1사분면
    if r < half and c < half:
        return func(n - 1, r, c)
    # 2사분면
    if r < half and c >= half:
        return half ** 2 + func(n - 1, r, c - half)
    # 3사분면
    if r >= half and c < half:
        return 2 * half ** 2 + func(n - 1, r - half, c)
    # 4사분면
    return 3 * half ** 2 + func(n - 1, r - half, c - half)

print(func(N,r,c))