import sys
input = sys.stdin.readline


def main():
    n = int(input())

    if n == 1 or n == 3:
        print(-1)
        return

    five = (n // 5) - 1 if (n % 5) & 1 else (n // 5)
    five_remain = n - 5 * five
    two = five_remain // 2

    print(five + two)


if __name__ == "__main__":
    main()
