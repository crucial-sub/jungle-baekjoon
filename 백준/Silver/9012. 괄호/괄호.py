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

def check_pairs(string):
    stack = Stack()
    for s in string:
        if s == "(":
            stack.push(s)
        else:
            if stack.is_empty():
                return "NO"
            stack.pop()
    if stack.is_empty():
        return "YES"
    else:
        return "NO"


def main():
    T = int(input())
    for _ in range(T):
        print(check_pairs(input().rstrip()))
        

if __name__ == "__main__":
    main()