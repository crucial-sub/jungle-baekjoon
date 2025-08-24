from collections import defaultdict
import sys
input = sys.stdin.readline

def main():
    N = int(input());

    tree = defaultdict(list);

    for _ in range(N-1):
        a, b = map(int, input().split());
        tree[a].append(b);
        tree[b].append(a);
    
    q = int(input());

    for _ in range(q):
        t, k = map(int, input().split());
        if t == 2:
            print('yes');
        elif t == 1:
            if len(tree[k]) == 1:
                print('no');
            else:
                print('yes');

if __name__ == "__main__":
    main()