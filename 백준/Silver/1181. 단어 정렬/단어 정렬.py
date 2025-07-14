import sys
N = int(sys.stdin.readline())
data = [sys.stdin.readline().rstrip() for _ in range(N)]
def sort_word(words: list[str]):
    max_len = max(len(word) for word in words)
    counting = [[] for _ in range(max_len)]
    for word in words:
        word_len = len(word)
        counting[word_len-1].append(word)

    sort_counting = [sorted(set(words)) for words in counting]

    return [word for sorted_words in sort_counting for word in sorted_words]

for word in sort_word(data):
    print(word)