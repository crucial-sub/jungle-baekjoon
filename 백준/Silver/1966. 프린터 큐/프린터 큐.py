from collections import deque
import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        docs = list(map(int, input().split()))
        sorted_docs = sorted(docs) # 우선순위로 정렬한 배열
        enumerate_docs = list(enumerate(docs))
        target = enumerate_docs[M]

        q = deque(enumerate_docs)
        cnt = 0

        while len(sorted_docs) > 0:
            cur = q.popleft()
            if cur[1] == sorted_docs[-1]:
                cnt += 1
                if cur == target:
                    print(cnt)
                    break
                sorted_docs.pop()
            else:
                q.append(cur)

if __name__ == "__main__":
    main()