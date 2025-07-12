import sys
N = int(sys.stdin.readline().rstrip());
input_data = [int(sys.stdin.readline()) for _ in range(N)]

def sort_merge(left, right) :
    i = 0;
    j = 0;
    sorted_list = []
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            sorted_list.append(right[j])
            j += 1;
        else : 
            sorted_list.append(left[i])
            i += 1;
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
        
    return sorted_list

def merge(input_list) :
    end = len(input_list);
    if end <= 1: return input_list

    mid = end//2
    left_list = merge(input_list[:mid])
    right_list = merge(input_list[mid:])
    return sort_merge(left_list,right_list);

for n in merge(input_data):
    print(n)
