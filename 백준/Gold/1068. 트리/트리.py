from collections import defaultdict
import sys
input = sys.stdin.readline

def main():
    N = int(input());
    parents = list(map(int, input().split()));
    erased = int(input());
    tree = defaultdict(list);
    root = 0;
    leaf_cnt = 0;

    for i in range(N):
        p = parents[i];
        if (p == -1):
            root = i;
            if erased == root:
                print(0);
                return;
            continue;
        tree[p].append(i);
    
    def erase_tree(n):
        if n not in parents:
            nonlocal leaf_cnt;
            leaf_cnt += 1;
        for child in tree[n]:
            if child != erased:
                erase_tree(child);
            else:
                if len(tree[n]) == 1:
                    leaf_cnt += 1;

    erase_tree(root);
    print(leaf_cnt);

if __name__ == "__main__":
    main()