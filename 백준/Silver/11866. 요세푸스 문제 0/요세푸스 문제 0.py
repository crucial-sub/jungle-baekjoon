from typing import Optional
import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = self

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def __iter__(self):
        if not self.head:
            return
        cur = self.head
        for _ in range(self._size):
            yield cur.data
            cur = cur.next

    def add_last(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            tail = self.head
            while tail.next is not self.head:
                tail = tail.next
            tail.next = new_node
            new_node.next = self.head
        self._size += 1

    def remove(self, idx):
        if not self.head:
            return
        cur = self.head
        for _ in range(idx-2):
            if cur is None:
                return
            cur = cur.next
        removed = cur.next
        cur.next = cur.next.next
        self.head = cur.next
        return removed.data

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    
    if K == 1:
        print("<" + ", ".join(map(str, [i for i in range(1,N+1)])) + ">")
    else:
        cll = CircularLinkedList()
        for i in range(1, N+1):
            cll.add_last(i)
        arr = []
        for _ in range(N):
            arr.append(cll.remove(K))

        print("<" + ", ".join(map(str, arr)) + ">")

        for i in range(-1):
            print(i)