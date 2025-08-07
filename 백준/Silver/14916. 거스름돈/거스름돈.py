import sys
input = sys.stdin.readline

def main():
    n = int(input())
    if n == 1 or n == 3:
        print(-1)
        return

    ans = 0

    if n%5 == 0:
        ans += n//5
    else:
        if (n%5) % 2 == 0:
            ans += n//5
            ans += (n%5)//2
        else:
            ans += (n//5)-1
            ans += ((n%5)+5)//2
    
    print(ans)

if __name__ == "__main__":
    main()