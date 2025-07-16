import sys
A, B, V = map(int, sys.stdin.readline().split())

last_day = 1;
move_per_day = A-B;
if (V-A) % move_per_day == 0:
    last_day = 1 + (V-A)//move_per_day
else:
    last_day = 1 + (V-A)//move_per_day + 1

print(last_day)