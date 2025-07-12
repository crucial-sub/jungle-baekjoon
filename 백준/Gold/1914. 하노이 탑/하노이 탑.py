import sys
N = int(sys.stdin.readline())

def move(n, start, target):
    if n == 0:
        return
    other = 6 - start - target
    move(n - 1, start, other)
    print(f"{start} {target}")
    move(n - 1, other, target)

print(2 ** N - 1)
if N <= 20:
    move(N, 1, 3)