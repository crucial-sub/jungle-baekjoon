from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def main():
    N = int(input());
    postfix = input().rstrip();

    oper = ["+","-","*","/"];
    val = {}
    stack = deque();
    calc_result = 0;

    for d in postfix:
        if d in oper:
            a = stack.pop();
            b = stack.pop();
            if d == "+": calc_result = b + a;
            if d == "-": calc_result = b - a;
            if d == "*": calc_result = b * a;
            if d == "/": calc_result = b / a;
            stack.append(calc_result);
        else:
            if d in val:
                n = val[d];
            else:
                n = int(input());
                val[d] = n
            stack.append(n);

    print(f"{calc_result:.2f}")

if __name__ == "__main__":
    main()