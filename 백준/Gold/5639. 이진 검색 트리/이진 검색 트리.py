from collections import defaultdict
import sys
input = sys.stdin.readline

class BinaryNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # 삽입 메서드
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
    def postorder_iter(self):
        if not self.root:
            return
        
        stack1 = [self.root]
        stack2 = []

        while stack1:
            # stack1에서 노드를 꺼내 stack2에 넣는다
            node = stack1.pop()
            stack2.append(node)

            # 꺼낸 노드의 자식들을 (존재한다면) stack1에 넣는다
            # ★★★ 왼쪽 먼저, 그 다음 오른쪽을 넣는 것이 핵심! ★★★
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        # stack2에 쌓인 노드들을 역순으로 출력하면 후위 순회 완성!
        while stack2:
            node = stack2.pop()
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

    bst.postorder_iter()
        


if __name__ == "__main__":
    main()