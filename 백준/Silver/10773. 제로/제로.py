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
        return self._data.pop()

    def peek(self):
        """스택 맨 위 요소 확인"""
        return self._data[-1]

    def is_empty(self) -> bool:
        """스택이 비어 있는지 검사"""
        return not self._data

def main():
    K = int(input())
    stack = Stack()
    for _ in range(K):
        n = int(input())
        if n != 0:
            stack.push(n)
        else:
            stack.pop()
    total = 0
    while not stack.is_empty():
        total += stack.pop()
    print(total)

if __name__ == "__main__":
    main()