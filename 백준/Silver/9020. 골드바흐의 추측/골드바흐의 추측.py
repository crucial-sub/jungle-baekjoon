import sys
T = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(T)]

def check_prime(n) :
    if(n < 2): return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False;
    return True;

for n in data:
    for i in range(n//2, 1-1, -1):
        if check_prime(i) and check_prime(n-i):
            print(f"{i} {n-i}");
            break;