import sys
input = sys.stdin.readline

N = int(input());

tree = {};

for _ in range(N):
    node, left_child, right_child = input().split()
    tree[node] = {
        "left": None if left_child == "." else left_child,
        "right": None if right_child == "." else right_child
    }

#전위 순회
# root-left-right
def preorder_traverse(n):
    if n == None:
        return;
    print(n, end='');
    preorder_traverse(tree[n]['left']);
    preorder_traverse(tree[n]['right']);

#중위 순회
# left-root-right
def inorder_traverse(n):
    if n == None:
        return;
    inorder_traverse(tree[n]['left']);
    print(n, end='');
    inorder_traverse(tree[n]['right']);

#후위 순회
# left-right-root
def postorder_traverse(n):
    if n == None:
        return;
    postorder_traverse(tree[n]['left']);
    postorder_traverse(tree[n]['right']);
    print(n, end='');

def main():
    preorder_traverse('A');
    print()
    inorder_traverse('A');
    print()
    postorder_traverse('A');

if __name__ == "__main__":
    main()