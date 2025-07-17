N = int(input())

count = 0;
str_n = str(N) if N >= 10 else f'0{N}'
new_num = str_n
while True:
    sum_n = str(sum(int(digit) for digit in new_num))[-1]
    right_n = new_num[-1]
    new_num = f'{right_n}{sum_n}'
    count += 1
    if new_num == str_n: break
print(count)