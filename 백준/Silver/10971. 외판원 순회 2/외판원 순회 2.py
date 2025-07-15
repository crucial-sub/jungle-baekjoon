import sys
from itertools import permutations
N = int(sys.stdin.readline())
data = [list(map(int,sys.stdin.readline().rstrip().split())) for i in range(N)]

def func(arr):
    cities = [city for city in range(N)]
    min_cost = float('inf')
    for p in permutations(cities):
        permu = list(p)
        permu.append(p[0])
        cost = 0
        for n in range(N):
            i = permu[n]
            j = permu[n+1]
            if arr[i][j] == 0:
                cost = float('inf')
                break
            cost += arr[i][j]
        min_cost = min(min_cost,cost)
        
    print(min_cost)
func(data)