import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self._data = []

    def push(self, x):
        """스택 맨 위에 x 추가"""
        self._data.append(x)

    def pop(self):
        """스택 맨 위 요소 제거 후 반환"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        """스택 맨 위 요소 확인"""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def is_empty(self) -> bool:
        """스택이 비어 있는지 검사"""
        return not self._data

def main():
    N = int(input())
    stack = Stack()
    for _ in range(N):
        h = int(input())
        stack.push(h)
    high = stack.pop()
    cnt = 1
    for _ in range(N-1):
        cur = stack.pop()
        if high < cur:
            high = cur
            cnt += 1
    print(cnt)

        

if __name__ == "__main__":
    main()