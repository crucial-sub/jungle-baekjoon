import sys
input = sys.stdin.readline

def main():
    K = int(input());
    tree = [[] for _ in range(K)];
    path = list(map(int, input().split()));

    for i in range(K):
        order = 2 ** (K - i -1);
        inc = 2 ** (K - i);
        while order < (2 ** K):
            tree[i].append(path[order-1]);
            order += inc;

    for depth in tree:
        print(*depth);

if __name__ == "__main__":
    main();