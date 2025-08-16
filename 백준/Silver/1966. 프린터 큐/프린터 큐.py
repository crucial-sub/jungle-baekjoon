from collections import deque
import sys
input = sys.stdin.readline

def main():
    T = int(input());
    for _ in range(T):
        N, M = map(int, input().split());
        docs = list(map(int, input().split()));
        docs_tuple = list(enumerate(docs));
        docs.sort()
        docs_q = deque(docs_tuple);
        cnt = 0;

        while(docs_q):
            doc = docs_q.popleft();
            if doc[1] == docs[-1]:
                cnt += 1;
                if doc == docs_tuple[M]:
                    print(cnt);
                    break;
                docs.pop();
            else:
                docs_q.append(doc);

if __name__ == "__main__":
    main()