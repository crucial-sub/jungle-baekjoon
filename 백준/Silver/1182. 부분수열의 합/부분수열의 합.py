import sys
input = sys.stdin.readline
N, S = map(int, input().split())
arr = list(map(int, input().split()))

count = 0

def backtrack(start, current_sum):
    global count
    for i in range(start,N):
        new_sum = current_sum + arr[i]
        if new_sum == S:
            count += 1
        backtrack(i+1, new_sum)

backtrack(0,0)

print(count)