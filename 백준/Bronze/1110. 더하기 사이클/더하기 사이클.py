import sys
N = int(sys.stdin.readline())

count = 0;
str_n = str(N) if N >= 10 else f'0{N}'
temp_n = str_n
while True:
    left_n = str(sum(int(digit) for digit in temp_n))[-1]
    right_n = temp_n[-1]
    temp_n = f'{right_n}{left_n}'
    count += 1
    if temp_n == str_n: break

print(count)