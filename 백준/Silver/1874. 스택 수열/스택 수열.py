from collections import deque
import sys
input = sys.stdin.readline

def main():
    N = int(input());
    sequence = [int(input().rstrip()) for _ in range(N)];

    i = 0; # 수열 인덱스
    n = 1; # 다음에 스택에 넣을 숫자
    stack = deque();
    ans = [];

    while(n <= N or stack):
        if n > N:
            if stack[-1] != sequence[i]:
                print("NO");
                return;
        if stack and (stack[-1] == sequence[i]):
            i += 1;
            stack.pop();
            ans.append('-')
            continue;
        stack.append(n);
        ans.append('+')
        n += 1;

    for a in ans:
        print(a)
        
if __name__ == "__main__":
    main()