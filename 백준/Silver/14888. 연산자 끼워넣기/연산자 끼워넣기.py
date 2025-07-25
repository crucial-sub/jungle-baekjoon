from collections import defaultdict, deque
from itertools import permutations
import sys
input = sys.stdin.readline

def oper_calc(oper,a,b):
    return {'+': a+b, '-': a-b, '*': a*b, '/': a//b if a > 0 else (a*(-1)//b)*(-1)}[oper] 

def main():
    N = int(input())
    arr_n = list(map(int,input().split()))
    arr_o = list(map(int, input().split()))
    opers =  ''.join([arr_o[i]*o for i,o in enumerate(['+','-','*','/'])])
    perm = set(permutations(opers,len(opers)))
    max_calc = float('-inf')
    min_calc = float('inf')
    for p in perm:
        total = arr_n[0]
        for i in range(0,N-1):
            total = oper_calc(p[i],total,arr_n[i+1])
        if total > max_calc:
            max_calc = total
        if total < min_calc:
            min_calc = total
        
    print(max_calc)
    print(min_calc)

if __name__ == "__main__":
    main()