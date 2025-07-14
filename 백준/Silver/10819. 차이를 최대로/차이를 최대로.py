from itertools import permutations
import sys
N = int(sys.stdin.readline())
data = map(int, sys.stdin.readline().split())

print(max([sum(abs(b - a) for a, b in zip(p, p[1:])) for p in permutations(data)]))