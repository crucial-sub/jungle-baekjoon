from collections import deque
import sys
input = sys.stdin.readline

def main():
    T = int(input());
    for _ in range(T):
        N, M = map(int, input().split());
        docs = list(map(int, input().split()));
        prior = sorted(docs,reverse=True);
        docs_tuple = list(enumerate(docs));

        prior_q = deque(prior)
        docs_q = deque(docs_tuple);
        cnt = 0;

        while(prior_q):
            doc = docs_q.popleft();
            if doc[1] == prior_q[0]:
                cnt += 1;
                if doc == docs_tuple[M]:
                    print(cnt);
                    break;
                prior_q.popleft();
            else:
                docs_q.append(doc);

if __name__ == "__main__":
    main()