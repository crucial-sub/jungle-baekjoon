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
        if self.empty():
            return -1
        return self._data.pop()

    def top(self):
        """스택 맨 위 요소 확인"""
        if self.empty():
            return -1
        return self._data[-1]

    def empty(self):
        """스택이 비어 있는지 검사"""
        return 1 if not self._data else 0

    def size(self):
        """스택 크기 확인"""
        return len(self._data)

def main():
    N = int(input())
    stack = Stack()
    for _ in range(N):
        oper = input().rstrip()
        if 'push' in oper:
            b = oper[5:]
            stack.push(b)
        else:
            print(getattr(stack, oper)())

if __name__ == "__main__":
    main()