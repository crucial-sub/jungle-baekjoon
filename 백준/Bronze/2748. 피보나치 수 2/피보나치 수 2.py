import sys
input = sys.stdin.readline

def main():
    n = int(input())

    if n <= 1:
        print(n)
        return
    
    dp_table = [0] * (n+1)

    dp_table[1] = 1

    for n in range(2, n+1):
        dp_table[n] =  dp_table[n-1] + dp_table[n-2]

    print(dp_table[n])

if __name__ == "__main__":
    main()