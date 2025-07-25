from collections import defaultdict
import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

class BinaryNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # --- 삽입 메서드 ---
    def insert(self, data):
        self.root = self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if node is None:
            return BinaryNode(data)
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        elif data > node.data:
            node.right = self._insert_recursive(node.right, data)
        return node

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
        # try-except 구문으로 파일 끝까지 입력을 받아 bst에 insert
        try:
            node = int(input().rstrip())
            bst.insert(node)
        except (ValueError, IndexError):
            # 빈 줄을 읽거나 더 이상 읽을 내용이 없으면 루프 종료
            break

    bst.postorder()
        


if __name__ == "__main__":
    main()