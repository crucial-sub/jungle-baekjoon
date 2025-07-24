from collections import defaultdict
import sys
input = sys.stdin.readline

class BinaryNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None  # 왼쪽 자식
        self.right = None # 오른쪽 자식

    # 전위 순회 메서드
    def preorder_traverse(self):
        # 1. Root(자기 자신) 방문
        print(self.data, end='')

        # 2. 왼쪽 자식이 있다면, 왼쪽 자식 노드에서부터 다시 전위 순회 시작
        if self.left: self.left.preorder_traverse()

        # 3. 오른쪽 자식이 있다면, 마지막으로 오른쪽 자식 노드에서부터 다시 전위 순회 시작
        if self.right: self.right.preorder_traverse()

        # 전위 순회를 언제 쓸까? 
        # 트리를 그대로 복사하거나, 폴더 구조를 그대로 출력할 때 유용!


    # 중위 순회 메서드
    def inorder_traverse(self):
        # 1. 왼쪽 자식이 있다면, 왼쪽 자식 노드에서부터 전위 순회 시작
        if self.left: self.left.inorder_traverse()
        
        # 2. Root(자기 자신) 방문
        print(self.data, end='')

        # 3. 오른쪽 자식이 있다면, 마지막으로 오른쪽 자식 노드에서부터 다시 전위 순회 시작
        if self.right: self.right.inorder_traverse()

        # 중위 순회를 언제 쓸까?
        # 이진 탐색 트리(Binary Search Tree)의 경우, 
        # 중위 순회를 하면 노드들이 오름차순으로 정렬되어 출력됨 
        # 정말 중요하고 신기한 특징이니 꼭 기억! ✨
        

    def postorder_traverse(self):
        # 1. 왼쪽 자식이 있다면, 왼쪽 자식 노드에서부터 후위 순회 시작
        if self.left: self.left.postorder_traverse()
        
        # 2. 오른쪽 자식이 있다면, 오른쪽 자식 노드에서부터 다시 후위 순회 시작
        if self.right: self.right.postorder_traverse()

        # 3. 마지막으로 Root(자기 자신) 방문
        print(self.data, end='')

        # 후위 순회를 언제 쓸까?
        # 자식 노드를 먼저 처리해야 하는 작업, 
        # 예를 들어 트리의 리프 노드부터 순서대로 삭제해야 할 때(메모리 해제) 사용!


def main():
    N = int(input())
    
    # BinaryNode를 기본 생성자로 하는 defaultdict를 생성합
    # 이제 tree는 존재하지 않는 키를 호출하면 BinaryNode 객체를 자동으로 생성
    tree = defaultdict(BinaryNode)

    for _ in range(N):
        node, left_child, right_child = input().split()

        # defaultdict 덕분에 data 키가 있는지 확인할 필요가 없음
        # tree[data]를 호출하는 순간, 없으면 BinaryNode(data)가 생성
        # 하지만 data는 항상 입력으로 주어지므로, 여기서는 그냥 값의 타입만 맞춰줌
        # 더 정확히는, BinaryNode의 data를 설정해주는 과정이 필요
        tree[node].data = node
        
        if left_child != '.':
            tree[left_child].data = left_child # 왼쪽 자식 노드의 데이터도 설정
            tree[node].left = tree[left_child]

        if right_child != '.':
            tree[right_child].data = right_child # 오른쪽 자식 노드의 데이터도 설정
            tree[node].right = tree[right_child]


    # 루트 노드는 항상 'A' 이므로 'A'에서 순회를 시작
    root_node = tree['A']

    root_node.preorder_traverse()
    print()
    root_node.inorder_traverse()
    print()
    root_node.postorder_traverse()
    print()


if __name__ == "__main__":
    main()