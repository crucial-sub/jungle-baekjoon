from collections import defaultdict
import sys
input = sys.stdin.readline

def main():
    K = int(input());
    tree = defaultdict(list);
    path = list(map(int, input().split()));

    for i in range(K):
        order = 2 ** (K - i -1);
        inc = 2 ** (K - i);
        while order < (2 ** K):
            tree[i].append(path[order-1]);
            order += inc;

    for i in range(K):
        print(*tree[i]);

if __name__ == "__main__":
    main();