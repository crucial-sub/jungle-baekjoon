import sys
x, y = map(int, sys.stdin.readline().split())
T = int(sys.stdin.readline())
data = [list(map(int,sys.stdin.readline().rstrip().split())) for i in range(T)]

x_list = [0,x];
y_list = [0,y];

for cut in data:
    cut_direction, cut_line = cut;
    if cut_direction == 0:
        y_list.append(cut_line);
        y_list.sort();
    else :
        x_list.append(cut_line);
        x_list.sort();

max_x_diff = 0
for i in range(1, len(x_list)):
    diff = x_list[i] - x_list[i-1]
    if diff > max_x_diff:
        max_x_diff = diff

max_y_diff = 0
for i in range(1, len(y_list)):
    diff = y_list[i] - y_list[i-1]
    if diff > max_y_diff:
        max_y_diff = diff
        
print(max_x_diff*max_y_diff)