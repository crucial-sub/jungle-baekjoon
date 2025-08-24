import sys
input = sys.stdin.readline

def main():
    K = int(input());
    path = list(map(int, input().split()));
    tree = [[] for _ in range(K)];

    def find_nodes(nodes, level):
        if not nodes:
            return;

        mid_idx = len(nodes) // 2
        root = nodes[mid_idx];
        tree[level].append(root);

        if level < (K - 1):
            find_nodes(nodes[:mid_idx], level + 1)
            find_nodes(nodes[mid_idx+1:], level + 1)

    find_nodes(path, 0);
    
    for depth in tree:
        print(*depth);

if __name__ == "__main__":
    main();