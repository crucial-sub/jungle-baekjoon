import sys
input = sys.stdin.readline

def main():
    board = input().rstrip().split(".")

    for i in range(len(board)):
        length = len(board[i])
        if length == 0:
            continue
        if length & 1:
            print(-1)
            return
        board[i] = "AAAA" * (length // 4) + "BB" * ((length % 4) // 2)

    print(".".join(board))


if __name__ == "__main__":
    main()
