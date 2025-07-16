import sys
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

ans = 0;
nums_odd = [x for x in nums if ((x % 2 != 0 and x != 1) or x == 2)];

for n in nums_odd:
    if n == 2 or n == 3:
        ans += 1
        continue
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        ans += 1
print(ans)