import sys
input = sys.stdin.readline
N, M = map(int, input().split())
m_arr = sorted(map(int, input().split()))

max_setting = 0
cur = -M;
    
def cut_tree(n):
    for i in reversed(range(n)):
        global max_setting, cur
        cur += m_arr[i]
        h_setting = int(cur/(N-i))
        max_setting = max(max_setting,h_setting)

cut_tree(N)

print(max_setting)