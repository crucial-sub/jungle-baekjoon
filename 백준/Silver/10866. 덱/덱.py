from collections import deque
import sys
input = sys.stdin.readline

def main():
    N = int(input());

    deq = deque()

    for _ in range(N):
        instruction = input().split();
        method = instruction[0];

        if method == "push_front":
            x = instruction[1];
            deq.appendleft(x);
        elif method == "push_back":
            x = instruction[1];
            deq.append(x);
        elif method == "pop_front":
            if not deq : print(-1);
            else : print(deq.popleft());
        elif method == "pop_back":
            if not deq : print(-1);
            else : print(deq.pop());
        elif method == "size":
            print(len(deq));
        elif method == "empty":
            if not deq : print(1);
            else : print(0);
        elif method == "front":
            if not deq : print(-1);
            else : print(deq[0])
        elif method == "back":
            if not deq : print(-1);
            else : print(deq[-1])

if __name__ == "__main__":
    main()