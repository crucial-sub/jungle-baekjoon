import sys
input = sys.stdin.readline

def main():
    n = int(input())

    if n <= 2:
        print(n)
        return
    
    dp_table = [0] * (n+1)

    dp_table[1] = 1
    dp_table[2] = 2

    for i in range(3, n+1):
        dp_table[i] =  (dp_table[i-1] + dp_table[i-2])%15746

    print(dp_table[n])

if __name__ == "__main__":
    main()