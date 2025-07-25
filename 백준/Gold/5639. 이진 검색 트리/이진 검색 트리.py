from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

class BinaryNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def inser_iter(self, node_val):
        node = BinaryNode(node_val)
        if not self.root:
            self.root = node
        else:
            cur = self.root
            while True:
                if node.data < cur.data:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = node
                        break
                elif node.data > cur.data:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = node      
                        break

    # 후위 순회 (왼쪽 -> 오른쪽 -> 루트)
    def postorder(self):
        self._postorder_recursive(self.root)

    def _postorder_recursive(self, node):
        if node:
            self._postorder_recursive(node.left)
            self._postorder_recursive(node.right)
            print(node.data)

def main():
    # 처음에 트리 생성
    bst = BinarySearchTree()

    while True:
        try:
            node = int(input().rstrip())
            bst.inser_iter(node)
        except (ValueError, IndexError):
            break

    bst.postorder()
        


if __name__ == "__main__":
    main()