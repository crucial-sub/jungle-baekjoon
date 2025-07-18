import sys
from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data # 노드가 포함할 실제 정보를 나타내는 값
        self.next = self # 다음 노드의 주소

    def __repr__(self):
        return repr(self.data)

class CircularLinkedList:
    def __init__(self):
        self.head = None # 연결리스트 초기화
        self._size = 0

    def __iter__(self):
        if not self.head:
            return
        cur = self.head
        for _ in range(self._size):
            yield cur.data
            cur = cur.next  # type: ignore

    def add_last(self,data):
        new_node = Node(data)
        if not self.head: # 리스트가 비어있는 경우 new_node를 head로 만들고 next에 자기자신 지정
            self.head = new_node
            new_node.next = self.head
        else:
            tail = self.head
            while tail.next is not self.head: # 헤드 직전 노드까지 계속 이동
                tail = tail.next
            tail.next = new_node # 찾은 노드의 next를 new_node로 연결
            new_node.next = self.head # new_node의 next로 헤드를 연결 
        self._size += 1

    #헤드를 1번으로 놓고 k번쨰 노드 제거
    def remove(self, k):
        if not self.head: # 리스트가 비어있으면 아무것도 하지 않음
            return
        prev = self.head # 지워야 할 노드의 직전 노드를 찾기 위해 for문 돌림
        steps = (k - 2) % cll._size
        for _ in range(steps):
            if prev is None:
                return
            prev = prev.next
        removed = prev.next
        prev.next = removed.next # 직전 노드의 next를 한단계 건너뛴 노드로 지정
        self.head = removed.next # 지우는 노드의 next를 헤드로 지정
        self._size -= 1
        return removed.data

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    cll = CircularLinkedList()
    for i in range(1, N+1):
        cll.add_last(i)
    arr = []
    for _ in range(N):
        arr.append(cll.remove(K))

    print("<" + ", ".join(map(str, arr)) + ">")