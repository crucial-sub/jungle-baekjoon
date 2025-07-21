from collections import deque
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    tops = enumerate(map(int, input().split()), start=1)
    stack = deque()
    result = [0] * N
    for i, h in tops:
        while stack and stack[-1][1] < h:
            stack.pop()
        result[i-1] = stack[-1][0] if stack else 0
        stack.append((i,h))
    print(*result)

if __name__ == "__main__":
    main()