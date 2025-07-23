import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    number_str = input().strip()
    
    stack = []
    k = K # 제거해야 할 숫자의 개수

    for digit in number_str:
        # 스택에 숫자가 있고, 아직 제거할 기회가 남았고,
        # 스택의 마지막 숫자가 현재 숫자보다 작으면
        while stack and k > 0 and stack[-1] < digit:
            stack.pop()
            k -= 1
        
        # 현재 숫자를 스택에 추가
        stack.append(digit)

    # 만약 k가 남아있다면(예: 98765 같은 내림차순 숫자),
    # 뒤에서부터 k개를 제거해야 가장 큰 수가 된다.
    # 최종 결과는 N-K 자리의 숫자여야 함.
    print(''.join(stack[:N-K]))


if __name__ == "__main__":
    main()