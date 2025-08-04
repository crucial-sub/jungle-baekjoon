from collections import deque
import sys
input = sys.stdin.readline

def main():
    expression = input()
    split_exp = [sum(map(int,x.split('+'))) for x in expression.split('-')]
    ans = split_exp[0]
    for i in range(1,len(split_exp)):
        ans -= split_exp[i]
    print(ans)

if __name__ == "__main__":
    main()