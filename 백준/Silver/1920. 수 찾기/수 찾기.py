import sys
input = sys.stdin.readline
N = int(input())
A = sorted(map(int, input().split()))
M = int(input())
arr_m = map(int, input().split())

def find_x(x, left, right):
    while left <= right:
        mid = (left+right)//2
        if A[mid] == x:
            print(1)
            return
        elif A[mid] < x:
            left = mid + 1
        else: 
            right = mid - 1
    print(0)

for m in arr_m:
    find_x(m, 0, N-1)