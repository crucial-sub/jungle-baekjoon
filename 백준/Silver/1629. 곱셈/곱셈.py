import sys
input = sys.stdin.readline

def recur(a,b,c):
    if b <= 2:
        return ((a%c)*(a%c))%c
    if b%2 == 0:
        half = recur(a,b//2,c)
        return half*half%c
    else:
        return (recur(a,b-1,c)*(a%c))%c

def main():
    A, B, C = map(int, input().split())
    if A == 1 or B == 1:
        print(A%C)
    else:
        print(recur(A,B,C))

if __name__ == "__main__":
    main()