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
    pairs = {"(": ")", "[": "]"}
    opener = {"(": 2, "[": 3}
    closer = {")": 2, "]": 3}
    string = input()
    stack = Stack()
    
    ans = 0
    val_cnt = 1
    
    for i,s in enumerate(string):
        if s in opener:
            stack.push(s)
            val_cnt *= opener[s]
        elif s in closer:
            if stack.is_empty():
                print(0)
                return
            top = stack.peek()
            if s != pairs[top]:
                print(0)
                return
            else:
                if string[i-1] == top:
                    ans += val_cnt
                stack.pop()
                val_cnt //= closer[s]
    if not stack.is_empty():
        print(0)
        return
    print(ans)

if __name__ == "__main__":
    main()