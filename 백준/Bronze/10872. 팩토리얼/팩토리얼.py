import sys
input_data = int(sys.stdin.readline().rstrip())

def facto(n):
    if n <= 1: return 1
    return n * facto(n-1)

print(facto(input_data))