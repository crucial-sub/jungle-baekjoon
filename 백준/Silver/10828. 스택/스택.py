import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self._data = []

    def push(self, x):
        """스택 맨 위에 x 추가"""
        self._data.append(x)
    
    def pop(self):
        """스택 맨 위 요소 제거 후 해당 요소 출력, 제거할 요소가 없을 시 -1 출력"""
        if self.empty():
            return -1
        return self._data.pop()

    def size(self):
        """스택 내 요소 갯수 출력"""
        return len(self._data)

    def empty(self):
        """스택이 비어있을 시 1, 아니면 0을 출력"""
        return 0 if self._data else 1

    def top(self):
        """스택 맨 위 요소 출력, 비어있을 시 -1 출력"""
        if self.empty():
            return -1
        return self._data[-1]

def main():
    N = int(input())
    stack = Stack()

    for _ in range(N):
        instruction = input().split()
        if len(instruction) == 2:
            stack.push(instruction[1])
        else:
            if hasattr(stack, instruction[0]):
                method = getattr(stack, instruction[0])
                print(method())

if __name__ == "__main__":
    main()